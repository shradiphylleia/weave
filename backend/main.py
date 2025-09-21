import uvicorn
from fastapi import FastAPI
from routers import marketing
from services.model_load import load_model

app = FastAPI(title="Marketing Copy Generator")

model, processor, device = load_model()

app.state.model = model
app.state.processor = processor
app.state.device = device

app.include_router(marketing.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
