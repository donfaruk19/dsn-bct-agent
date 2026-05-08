import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class UserModeler:
    def __init__(self):
        # Using Groq for high-throughput to stay within hackathon performance limits
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_persona(self, history):
        """Builds a Nigerian-centric consumer profile."""
        history_str = str(history)
        prompt = f"""
        Analyze this purchase history: {history_str}
        Create a detailed consumer persona for a Nigerian user. 
        Identify their lifestyle, income bracket, and cultural buying motivations.
        Output your response as a descriptive paragraph.
        """
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content

    def simulate_review(self, persona, prod_name, prod_desc):
        """TASK A: Simulates star rating and text based on persona."""
        prompt = f"""
        USER PERSONA: {persona}
        NEW PRODUCT: {prod_name}
        DESCRIPTION: {prod_desc}

        Based on this persona, simulate a review this user would write for this product.
        Output ONLY a JSON object with:
        1. "star_rating": (Integer 1-5)
        2. "review_text": (A review written in the user's specific Nigerian tone and context)
        """
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return json.loads(completion.choices[0].message.content)