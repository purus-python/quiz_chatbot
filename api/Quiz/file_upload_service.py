import os
from fastapi import APIRouter, UploadFile, File, HTTPException, Form, Depends
from fastapi.responses import JSONResponse
from datetime import datetime
from sqlalchemy.orm import Session
from api.common.database_utils import get_db
from api.common.quiz_question_generations import get_answer_from_pinecone
from api.common.quiz_fileupload import extract_text_from_pdf

# Create a router
quiz_chat_router = APIRouter(prefix="/quiz-chat", tags=["Quiz Chat"])

# Define the folder where files will be stored locally
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the folder exists

# @quiz_chat_router.post("/", summary="Upload a file and generate quiz questions")
# async def quiz_chat_handler(
#     question: str = Form(...),
#     file: UploadFile = File(...),
#     db: Session = Depends(get_db)
# ):
#     try:
#         # Build file path in local uploads folder
#         file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        
#         # Check if file already exists locally
#         if not os.path.exists(file_path):
#             with open(file_path, "wb") as out_file:
#                 content = await file.read()
#                 out_file.write(content)
        
#         # Convert PDF to text
#         assignment_text = extract_text_from_pdf(file_path)
        
#         # Call get_answer_from_pinecone passing the db session
#         response_data = await get_answer_from_pinecone(question, assignment_text, db)
        
#         return JSONResponse(content={"success": True, "data": response_data}, status_code=200)

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@quiz_chat_router.post("/", summary="Upload a file and generate quiz questions")
async def quiz_chat_handler(
    question: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        if not os.path.exists(file_path):
            with open(file_path, "wb") as out_file:
                content = await file.read()
                out_file.write(content)
        
        assignment_text = extract_text_from_pdf(file_path)
        response_data = await get_answer_from_pinecone(question, assignment_text, db)
        # Assuming get_answer_from_pinecone returns a dict with at least "question", "answer", "score".
        # We'll also include the file name in our response.
        response_data["file_name"] = file.filename
        
        return JSONResponse(content={"success": True, "data": response_data}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
