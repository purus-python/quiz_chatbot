**Quiz Chatbot - Project Overview**

**Project Structure**

1. Root Directory: app/

This is the main project folder that contains all necessary files and subdirectories.

2. quiz/ Folder (Core Functionality)

File: file_upload_service.py

Purpose:

Allows users to upload PDF files.

Extracts questions from the uploaded document and converts them into JSON format for chatbot processing.

Users can continuously ask questions based on the uploaded document.

Limitation:

If no PDF file is uploaded, the API will return an error.

3. common/ Folder (Shared Utilities)

File: openai_methods.py

Purpose:

Analyzes user-uploaded documents and questions.

Uses OpenAI to generate responses based on document content.

Response Validation: If a question is unrelated to the document, it returns:"Your question is not related to the document. Please ask a relevant question."

File: config.py

Purpose:

Stores common credentials and configuration settings used across the project.

Allows reusability and centralized management of environment variables.

File: database_utils.py

Purpose:

Provides database connection credentials for seamless interaction with the database.

File: pinecone_configuration.py

Purpose:

Implements logic to establish a connection with the Pinecone vector database.

Enables semantic search for retrieving relevant data from stored vectors.

File: prompt_store.py

Purpose:

Defines chatbot prompting logic.

Determines how the chatbot formulates responses.

File: quiz_fileupload.py

Purpose:

Converts PDF documents to text using the fitz Python package (PyMuPDF).

File: quiz_question_validation.py

Purpose:

Validates uploaded questions and documents.

Step 1: Checks if a similar question already exists in the vector database.

If a match is found → retrieves answer from vector database.

Otherwise → Calls OpenAI to analyze if the question is relevant to the document before generating an answer.

File: response_utils.py

Purpose:

Ensures that API responses follow proper JSON format.

Validates response correctness before returning output.

4. models/ Folder (Database Models - ORM)

Purpose:

Implements Object-Relational Mapping (ORM).

Defines database tables and their structure.

5. uploads/ Folder (File Storage)

Purpose:

Stores uploaded files (currently supports .pdf format only).

File: input_test.json

Purpose:

Contains sample API input data for automated testing.

Eliminates the need for manual API testing.

6. testing/ Folder (Automated Testing)

Purpose:

Ensures all API functionalities work correctly.

Reduces manual testing efforts by running pre-defined test cases.

File: automation.py

Purpose:

Implements automated testing for API validation.

Provides various test scenarios.

Generates a test report showing how many cases passed and failed.

7. app.py (API Entry Point)

Purpose:

The main FastAPI application file.

Allows testing through Postman.

Implements API endpoints to validate inputs and outputs.

Usage:

Run app.py to start the FastAPI server.

Use Postman to test API endpoints.

Ensures all implemented methods work correctly.

Testing and Validation

Manual Testing:

Use Postman to check API responses.

Automated Testing:

Run pytest to validate multiple test cases without manual intervention.

Ensures the API returns correct responses for different scenarios.

Summary

This project allows users to upload PDF files and ask questions related to the document.

The chatbot uses OpenAI and Pinecone to analyze and retrieve responses.

Automated testing ensures all API functionalities work correctly.

Common utilities are centralized in the common/ folder for efficiency.
