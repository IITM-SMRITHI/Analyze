"""Main Application Entry Point

FastAPI-based data analysis service that provides REST API endpoints
for analyzing datasets, generating visualizations, and creating reports.
"""

import logging
import sys
from pathlib import Path
from typing import Dict, Any
import uvicorn
from fastapi import FastAPI, HTTPException, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field
import pandas as pd
import numpy as np

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Analyze - Data Analysis Service",
    description="A comprehensive data analysis service for statistical analysis, visualization, and reporting.",
    version="1.0.0",
    contact={
        "name": "IITM-SMRITHI",
        "email": "23f3004253@ds.study.iitm.ac.in"
    }
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalysisRequest(BaseModel):
    """Request model for data analysis"""
    email: EmailStr = Field(..., description="Email address for notifications")
    dataset_name: str = Field(..., description="Name of the dataset to analyze")
    analysis_type: str = Field(default="comprehensive", description="Type of analysis: descriptive, statistical, or comprehensive")
    include_visualization: bool = Field(default=True, description="Whether to include visualizations")


class AnalysisResponse(BaseModel):
    """Response model for analysis results"""
    task_id: str
    status: str
    message: str
    email: str


@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Analyze - Data Analysis Service",
        "version": "1.0.0",
        "email": "23f3004253@ds.study.iitm.ac.in"
    }


@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze_data(
    request: AnalysisRequest,
    background_tasks: BackgroundTasks
):
    """Endpoint to submit data analysis tasks"""
    logger.info(f"Received analysis request for dataset: {request.dataset_name} from {request.email}")
    
    task_id = f"{request.dataset_name}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Here you would add background task processing
    # background_tasks.add_task(process_analysis, request, task_id)
    
    return AnalysisResponse(
        task_id=task_id,
        status="accepted",
        message=f"Analysis task '{task_id}' has been accepted and is being processed.",
        email=request.email
    )


@app.get("/api/status/{task_id}")
async def get_task_status(task_id: str):
    """Get the status of an analysis task"""
    return {
        "task_id": task_id,
        "status": "processing",
        "progress": "50%"
    }


@app.get("/statistics")
async def get_statistics():
    """Get service statistics"""
    return {
        "total_analyses": 0,
        "active_tasks": 0,
        "completed_tasks": 0,
        "uptime_hours": 0
    }


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler"""
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": str(exc),
            "path": str(request.url)
        }
    )


if __name__ == "__main__":
    logger.info("Starting Analyze service...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
