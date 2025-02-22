import json
from datetime import datetime
from api.common.prompt_store import quiz_prompt
from api.common.openai_methods import ask_to_openai
from api.common.pinecone_configuration import pc, index, model, PINECONE_INDEX_NAME
from api.common.database_utils import get_db  # This is an async generator for AsyncSession
from api.models.question_upload_model import QuizChatModel
from sentence_transformers import SentenceTransformer
from sqlalchemy.ext.asyncio import AsyncSession


qa_pairs = []
current_time = datetime.now()

current_time = datetime.now()
async def save_question_answer(qa_pairs: list, db: AsyncSession) -> int:
    if PINECONE_INDEX_NAME not in pc.list_indexes().names():
        print(f"Pinecone index '{PINECONE_INDEX_NAME}' created")
    else:
        print(f"Pinecone index '{PINECONE_INDEX_NAME}' already exists")
    
    # Connect to the existing Pinecone index
    index = pc.Index(PINECONE_INDEX_NAME)
    # For embedding generation, we use SentenceTransformer
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    
    vectors = []
    # Loop over each QA pair and prepare vector records and database records.
    for i, item in enumerate(qa_pairs):
        # Generate embedding for the question
        embedding = embed_model.encode(item["question"]).tolist()
        record_id = f"qa_{i+1}"  # Unique ID for each record
        
        vectors.append((record_id, embedding, {"question": item["question"], "answer": item["answer"]}))
        
        new_answer = QuizChatModel(
            quiz_notes=item,  # You can adjust this field to store your QA pair or additional details
            active=True,
            created_on=current_time,
            updated_on=current_time
        )
        db.add(new_answer)
    
    db.add(new_answer)
    await db.commit()  # Make sure to await commit
    await db.refresh(new_answer)
    
    index.upsert(vectors)
    
    return len(qa_pairs)

async def get_answer_from_pinecone(question: str, assignment_text: str, db: AsyncSession) -> dict:
    # Generate embedding for the query (assuming model is globally defined)
    query_embedding = model.encode(question).tolist()
    
    # Query the Pinecone index for similar questions
    result = index.query(vector=query_embedding, top_k=1, include_metadata=True)
    results_data = None
    
    if result and result.get("matches"):
        match = result["matches"][0]
        score = match["score"]
        # If the similarity score is above the threshold, use the stored answer.
        if score > 0.65:
            matched_qa = match["metadata"]
            response_answer = matched_qa.get("answer", "")
            results_data = {"question": question, "answer": response_answer, "score": score}
            new_answer = QuizChatModel(
                quiz_notes=results_data,
                active=True,
                created_on=current_time,
                updated_on=current_time
            )
            db.add(new_answer)
            await db.commit()
            await db.refresh(new_answer)
    
    # If no match is found, fall back to OpenAI logic
    if results_data is None:
        print("No high similarity match found; calling OpenAI logic")
        prompt = quiz_prompt['prompt'].replace('{question}', question).replace('{assignment_text}', assignment_text)
        system_content = quiz_prompt['system_content'].replace('{assignment_text}', assignment_text)
        
        # Call OpenAI to get an answer (assumes ask_to_openai returns a JSON string)
        results = ask_to_openai(prompt, system_content)
        response_data = json.loads(results)
        print(response_data)
        if response_data.get("score", 0) > 0:
            qa_pairs.append(response_data)
            # Save all new qa_pairs to the database in one go.
            for item in qa_pairs:
                new_answer = QuizChatModel(
                    Quiz_notes=item,
                    active=True,
                    created_on=current_time,
                    updated_on=current_time
                )
                db.add(new_answer)
            await db.commit()
            results_data = response_data
        else:
            results_data = {
                "question": question,
                "answer": "This question is not related to the uploaded document; please ask a related question."
            }
    
    return results_data