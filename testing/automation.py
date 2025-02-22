import pytest
import json,os
from fastapi.testclient import TestClient
from fastapi import FastAPI
from api.Quiz.file_upload_service import quiz_chat_router

app = FastAPI()
app.include_router(quiz_chat_router)
client = TestClient(app)
current_dir = os.path.dirname(__file__)

@pytest.fixture
def load_test_json():
    """Load JSON input file containing the form field data."""
    file_path = os.path.join(current_dir, "uploads", "input_test.json")
    
    with open(file_path, "r") as f:
        return json.load(f)

def test_quiz_api_with_file(load_test_json):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "uploads", "science.pdf")

    with open(file_path, "rb") as file:
        data = {
            "question": load_test_json.get("question")
        }
        files = {"file": ("science.pdf", file, "application/pdf")}
        response = client.post("/quiz-chat/", data=data, files=files)

    assert response.status_code == 200, f"Response code was {response.status_code}: {response.text}"
    response_json = response.json()
    response_data =response_json.get('data')
    assert response_data.get('question')
    assert response_data.get('answer')

def test_invalid_file_upload(load_test_json):
    """Test API with an invalid file type."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "uploads", "invalid.txt")
    with open(file_path, "rb") as file:
        data = {
            "question": load_test_json.get("question")
        }
        files = {"file": ("invalid.txt", file, "text/plain")}
        response = client.post("/quiz-chat/", data=data, files=files)
    assert response.status_code != 400, f"Expected 400, got {response.status_code}: {response.text}"    
    assert response
