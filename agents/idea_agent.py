import openai
import os

class IdeaAgent:
    """
    Agent to generate creative research/model ideas using GPT-4o via OpenAI API.
    """
    def __init__(self, api_key=None):
        """
        Args:
            api_key (str): OpenAI API key. If None, reads from OPENAI_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def generate_idea(self, research_prompt):
        """
        Queries GPT-4o to generate a creative research/model idea.

        Args:
            research_prompt (str): Description of the research goal/benchmark to beat.
        Returns:
            str: Generated idea/plan.
        """
        messages = [
            {"role": "system", "content": "You are a creative AI research scientist. Respond with a concrete, novel model idea or strategy for the given research goal."},
            {"role": "user", "content": research_prompt}
        ]
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=messages,
                temperature=1.6,
                max_tokens=500,
            )
            idea = response.choices[0].message.content.strip()
            return idea
        except Exception as e:
            return f"[ERROR] Failed to generate idea: {e}"

