from pydantic import BaseModel
from typing import List, Dict, Any

# Response DTO
class QuizQuestionResponseDTO(BaseModel):
    success: bool
    data: dict