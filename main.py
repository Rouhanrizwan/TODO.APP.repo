import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as routes_app

# Create FastAPI app instance
app = FastAPI(title="Todo API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(routes_app)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Todo API is running!"}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}