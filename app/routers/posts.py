# app/routers/posts.py
from .. import models
from fastapi import APIRouter, Form
from pydantic import BaseModel
from app.agents.harvesting_agent import analyze_feasibility
from app.models import CostRequest, FeasibilityRequest
from app.agents.cost_agent import analyze_cost_and_schemes

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/feasibility")
def check_feasibility(payload: FeasibilityRequest):
    # Now payload is a Pydantic model parsed from JSON body
    result = analyze_feasibility(payload.location, payload.roof_area, payload.open_space)
    return {"status": "success", "analysis": result}

@router.post("/cost-analysis")
def cost_analysis(payload: CostRequest):
    result = analyze_cost_and_schemes(payload.harvesting_type, payload.location)
    return {"status": "success", "cost_analysis": result}





