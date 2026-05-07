import os
from google import genai
from dotenv import load_dotenv

load_dotenv()


class UserModeler:
    def __init__(self):
        # The client automatically looks for GEMINI_API_KEY in your .env
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.model_id = "gemini-1.5-flash"

    def generate_persona(self, raw_history):
        """
        Task A: Behavioral Fidelity Module.
        Refined to capture 'Naija' nuance as per the hackathon brief.
        """
        prompt = f"""
        Act as a Nigerian consumer behavior expert. Analyze this review history:
        {raw_history}

        Create a 'Digital Persona' that captures:
        1. Linguistic Style: (e.g., Use of words like 'Standard', 'Oshey', or formal Nigerian English).
        2. Core Values: (e.g., Does the user prioritize durability because of local conditions?).
        3. Rating Bias: (Are they stingy with 5-stars?).

        Return the result in a clean JSON format.
        """

        response = self.client.models.generate_content(
            model=self.model_id,
            contents=prompt
        )
        return response.text