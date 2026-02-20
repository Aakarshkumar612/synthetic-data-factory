import streamlit as st
import pandas as pd
from generator import generate_data
from src.processor import parse_raw_data, convert_to_jsonl

st.set_page_config(page_title="Synthetic Data Factory Pro", page_icon="🏭", layout="wide")

st.title("🏭 Synthetic Data Factory Pro")

with st.sidebar:
    st.header("Control Panel")
    topic = st.text_input("Niche Topic", placeholder="e.g., Python 3.12 Decorators")
    num_pairs = st.slider("Samples to Generate", 1, 20, 5)
    generate_btn = st.button("Start Production Line", type="primary")

if generate_btn:
    if not topic:
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Gemini is crafting expert data..."):
            raw_text = generate_data(topic, num_pairs)
            df = parse_raw_data(raw_text)
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Raw API Response")
                st.text_area("Log", raw_text, height=400)
            
            with col2:
                st.subheader("Structured Dataset")
                st.dataframe(df, use_container_width=True)
                
                # --- DOWNLOAD OPTIONS ---
                # CSV for human reading
                csv_data = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download CSV (For Review)",
                    data=csv_data,
                    file_name=f"{topic}_data.csv",
                    mime="text/csv"
                )
                
                # JSONL for Phi-3 Fine-Tuning
                jsonl_data = convert_to_jsonl(df)
                st.download_button(
                    label="Download JSONL (For Fine-Tuning)",
                    data=jsonl_data,
                    file_name=f"{topic}_tuning.jsonl",
                    mime="application/jsonl"
                )

st.divider()
st.info("Pipeline: Gemini 2.5 Flash (Teacher) -> Regex Parser -> Phi-3 Ready JSONL.")