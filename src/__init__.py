from fastapi import FastAPI
from .routes import router
app = FastAPI(
    title="HNG Stage 0 API",
    description="Endpoint for HNG Stage 0 task"
)


app.include_router(router)