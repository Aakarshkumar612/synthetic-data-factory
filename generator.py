import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

def generate_data(topic: str, count: int = 5) -> str:
    """Generates synthetic data using the verified Gemini 2.5 Flash model."""
    
    # Pro Tip: Always use the 'v1' stable channel for Tier 1 reliability
    with genai.Client(
        api_key=GEMINI_KEY,
        http_options=types.HttpOptions(api_version='v1')
    ) as client:
        
        prompt = f"""
        Act as a senior technical educator. Generate {count} high-quality 
        Question and Answer pairs about '{topic}'.
        
        Format each pair exactly like this:
        Q: [Question]
        A: [Answer]
        ---
        """
        
        try:
            # Using the model YOUR terminal confirmed: gemini-2.5-flash
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"API Error: {str(e)}"

if __name__ == "__main__":
    print("🚀 Factory Line: Using Verified Gemini 2.5 Flash...")
    print(generate_data("SQL Window Functions", count=1))