from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from persona import UserModeler
from recommender import AgenticRecommender
from data_utils import load_and_clean_data, get_user_history

app = FastAPI(title="BCT Hackathon: AI Agent")

# Initialize our components
user_modeler = UserModeler()
recommender = AgenticRecommender()
df = load_and_clean_data("amazon.csv")


class RecommendationRequest(BaseModel):
    user_id: str


@app.get("/")
def home():
    return {"status": "Agent is online", "challenge": "BCT LLM Agent Hackathon"}


@app.post("/task-a/model-user")
def model_user(request: RecommendationRequest):
    """Generates a Nigerian-style persona from history."""
    history = get_user_history(df, request.user_id)
    if not history:
        raise HTTPException(status_code=404, detail="User not found")

    persona = user_modeler.generate_persona(history)
    return {"user_id": request.user_id, "persona": persona}


@app.post("/task-b/recommend")
def get_recommendations(request: RecommendationRequest):
    """Reasons and then recommends."""
    history = get_user_history(df, request.user_id)
    persona = user_modeler.generate_persona(history)

    # We take a sample of products from the catalog to recommend from
    catalog_sample = df[['product_name', 'category', 'about_product']].sample(5).to_dict()

    suggestion = recommender.recommend(persona, catalog_sample)
    return {"recommendation": suggestion}
