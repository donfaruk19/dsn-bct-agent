"""
Task B: Recommendation Engine.
Implements Agentic Reasoning to provide contextualized Nigerian product suggestions.
"""
# 1. Analyze user persona
# 2. Match with local infrastructure constraints (Power/Data etc)
# 3. Generate cross-domain pairings (Food/Culture)
import os
from groq import Groq


class AgenticRecommender:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def recommend(self, persona, catalog):
        """TASK B: Rank and recommend with agentic reasoning."""
        prompt = f"""
        User Persona: {persona}
        Available Catalog Items: {str(catalog)}

        INSTRUCTIONS:
        1. Analyze the user's local context (Nigeria: power, costs, durability etc).
        2. Evaluate the catalog items.
        3. Recommend the BEST item.
        4. Provide 'Reasoning' for the choice.
        5. Suggest one 'Cross-Domain' item (e.g., a specific Nigerian food, movie, culture, drink etc) that pairs with this choice.

        Output format:
        Recommended Item: [Name]
        Reasoning: [Why this fits the Nigerian context]
        Cross-Domain Suggestion: [Complementary local item]
        """

        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
