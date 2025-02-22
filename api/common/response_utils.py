from fastapi.responses import JSONResponse

def prepare_json_response(data: dict, code: int, headers: dict = None) -> JSONResponse:
    return JSONResponse(content=data, status_code=code, headers=headers or {})