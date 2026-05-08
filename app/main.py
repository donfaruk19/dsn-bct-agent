"""
Main API Gateway for the BCT AI Agent.
Handles Task A (User Modeling) and Task B (Recommendation).
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .persona import UserModeler
from .recommender import AgenticRecommender
from .data_utils import load_and_clean_data, get_user_history

app = FastAPI(title="DSN-BCT Consumer AI Agent", version="1.0.0")

# Initialize components
user_modeler = UserModeler()
recommender = AgenticRecommender()
df = load_and_clean_data("amazon.csv")


class ReviewSimulationRequest(BaseModel):
    user_id: str
    product_name: str
    product_description: str


class RecommendRequest(BaseModel):
    user_id: str


@app.get("/")
def health_check():
    return {"status": "Agent Online", "task": "BCT LLM Hackathon"}


@app.post("/task-a/simulate")
def task_a_simulation(request: ReviewSimulationRequest):
    """Generates behavioral-faithful reviews and ratings."""
    history = get_user_history(df, request.user_id)
    if not history:
        raise HTTPException(status_code=404, detail="User History Not Found")

    # Token Optimization: Use last 3 items for persona
    persona = user_modeler.generate_persona(history[-3:])

    simulation = user_modeler.simulate_review(
        persona, request.product_name, request.product_description
    )

    return {
        "user_id": request.user_id,
        "persona_applied": persona[:150] + "...",
        "simulation": simulation
    }


@app.post("/task-b/recommend")
def task_b_recommendation(request: RecommendRequest):
    """Delivers contextual, cross-domain recommendations[cite: 3]."""
    history = get_user_history(df, request.user_id)
    if not history:
        raise HTTPException(status_code=404, detail="User History Not Found")

    # Build Persona
    persona = user_modeler.generate_persona(history[-3:])

    # Contextual Retrieval: Sample 5 items from catalog
    catalog_sample = df[['product_name', 'category']].sample(5).to_dict(orient='records')

    # Agent Reasoning
    recommendation = recommender.recommend(persona, catalog_sample)

    return {
        "user_id": request.user_id,
        "recommendation_engine_output": recommendation
    }