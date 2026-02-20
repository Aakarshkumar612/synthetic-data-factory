import os
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Load local .env file (if it exists)
load_dotenv()

def get_api_key():
    """
    Safely retrieves the API key from Environment or Streamlit Secrets.
    This prevents StreamlitSecretNotFoundError.
    """
    # First, try standard environment variables (Local dev)
    key = os.getenv("GEMINI_API_KEY")
    
    # If not found, try Streamlit secrets (Cloud dev)
    if not key:
        try:
            # We use .get() to avoid the crash if the secret is missing
            key = st.secrets.get("GEMINI_API_KEY")
        except Exception:
            key = None
            
    return key

# Initialize the key
GEMINI_KEY = get_api_key()

def generate_data(topic: str, count: int = 5) -> str:
    """Generates synthetic data using the verified Gemini 2.5 Flash model."""
    
    if not GEMINI_KEY:
        return "❌ Error: Gemini API Key not found. Please check your .env file or Streamlit Secrets."

    # Using 'with' ensures the connection is closed properly
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
            # Verified model from your terminal health check
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"⚠️ API Error: {str(e)}"

if __name__ == "__main__":
    print("🚀 Factory Line: Running Internal Health Check...")
    print(generate_data("Python 3.12 Syntax", count=1))