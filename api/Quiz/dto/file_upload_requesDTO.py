from pydantic import BaseModel
from typing import List

# Request DTO
class QuizQuestionRequestDTO(BaseModel):
    studentname: str
    studentid: int