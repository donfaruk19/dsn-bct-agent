import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class UserModeler:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_persona(self, raw_history):
        """
        Task A: Transforms raw Amazon/Yelp history into a
        sophisticated behavioral profile.
        """
        prompt = f"""
        Analyze the following user review history: {raw_history}

        Create a detailed User Persona JSON including:
        1. Tone (e.g., sarcastic, enthusiastic, brief)
        2. Rating Bias (e.g., hard to please, easy 5-stars)
        3. Local Context: Adapt this persona to sound like a Nigerian user 
           (e.g., mention data costs, power reliability, or local slang where relevant) [cite: 12].

        Return ONLY a JSON object.
        """
        response = self.model.generate_content(prompt)
        return response.text
# User Modeling logic (Task A)
