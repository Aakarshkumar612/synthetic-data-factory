# 🏭 Synthetic Data Factory Pro

A professional-grade pipeline that uses **Gemini 2.5 Flash** (The Teacher) to generate high-quality synthetic datasets for fine-tuning smaller models like **Phi-3** (The Student).

## 🚀 Features
* **Teacher-Student Distillation:** Leverage frontier models to train specialized "tiny" models.
* **Stable v1 API Integration:** Uses the most reliable Gemini 1.5/2.5 Flash endpoints.
* **Auto-Parsing:** Uses Regex to transform raw LLM text into structured DataFrames.
* **Fine-Tuning Ready:** Export your data directly to `.jsonl` (JSON Lines), the industry standard for LLM training.

## 🛠️ Tech Stack
* **Language:** Python 3.12 (Conda Environment)
* **AI:** Google Gemini API (google-genai SDK)
* **Frontend:** Streamlit
* **Data:** Pandas & Regex

## 📦 Setup Instructions


1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/synthetic-data-factory.git](https://github.com/your-username/synthetic-data-factory.git)
   cd synthetic-data-factory

2. Create Environment:
   conda create -n synthetic_env python=3.12 -y
   conda activate synthetic_env

3. Install Dependencies:   
   pip install -r requirements.txt

4. Environment Variables:
   Create a .env file in the root directory and add your key:
   GEMINI_API_KEY=your_key_here


5. Run the App:
   streamlit run app.py

 📄 License
     MIT
 
