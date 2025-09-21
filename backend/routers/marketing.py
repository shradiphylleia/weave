from fastapi import APIRouter, Request
from models.marketing_request import MarketingRequest
from services.generator import generate_marketing_copy_service

router = APIRouter()

@router.post("/generate-copy/")
async def generate_copy(request_data: MarketingRequest, request: Request):
    model = request.app.state.model
    processor = request.app.state.processor
    device = request.app.state.device

    if not model or not processor:
        return {"error": "Model not loaded. Please check the server logs."}

    copy = generate_marketing_copy_service(request_data, model, processor, device)
    return {"copy": copy}
