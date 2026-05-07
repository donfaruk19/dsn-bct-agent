from google import genai
import os


class AgenticRecommender:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def recommend(self, persona_json, products):
        """
        Task B: Conversational Retrieval & Reasoning.
        """
        prompt = f"""
        System: You are an expert Recommender Agent. 
        You must REASON step-by-step before suggesting a product.

        User Persona: {persona_json}
        Product Catalog: {products}

        Instructions:
        1. Analyze the Persona's specific Nigerian context.
        2. Evaluate the products based on that context.
        3. Suggest the top item and explain 'Why' using the user's 'vibe'.
        """

        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text