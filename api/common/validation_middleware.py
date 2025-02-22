# Middleware for Request Validation
from fastapi import FastAPI, Request, HTTPException, Depends
from pydantic import BaseModel, ValidationError

async def request_validation_middleware(request: Request, schema: BaseModel):
    try:
        data = await request.json()
        return schema(**data)
    except ValidationError as err:
        raise HTTPException(status_code=400, detail={"success": False, "validation_errors": err.errors()})