import re
import pandas as pd

def parse_raw_data(raw_text: str) -> pd.DataFrame:
    """
    Parses raw Gemini text into a structured Pandas DataFrame.
    """
    # Regex to find Q&A pairs regardless of extra newlines
    pattern = r"Q:(.*?)A:(.*?)(?=---|$)"
    matches = re.findall(pattern, raw_text, re.DOTALL)
    
    data = []
    for q, a in matches:
        data.append({
            "instruction": q.strip(),
            "response": a.strip()
        })
    
    return pd.DataFrame(data)

def convert_to_jsonl(df: pd.DataFrame) -> str:
    """
    Converts DataFrame to JSON Lines string for fine-tuning.
    """
    # orient='records' and lines=True is the standard for LLM datasets
    return df.to_json(orient='records', lines=True)