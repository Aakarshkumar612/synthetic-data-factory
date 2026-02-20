# 🏭 Synthetic Data Factory Pro

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://synthetic-data-factory-6kh6annvfj8h4ej57mkqdm.streamlit.app/)

A professional-grade AI pipeline designed to generate high-quality synthetic datasets. This project implements a **Teacher-Student Distillation** workflow, using frontier models to create specialized training data for smaller, efficient models like **Phi-3**.

## 🎯 The Concept
Don't just fine-tune a model; build the dataset. This factory uses **Gemini 2.5 Flash** (The Teacher) to generate thousands of high-quality Question/Answer pairs, filters them for quality, and exports them into structured formats to outperform giant models on specific tasks.


## 🚀 Key Features
* **Intelligent Generation:** Leverages Gemini 2.5 Flash for high-density, technical data generation.
* **Regex-Powered Parsing:** Automatically transforms messy LLM text into clean Pandas DataFrames.
* **Fine-Tuning Ready:** Direct export to `.jsonl` (JSON Lines), the industry standard for LLM training pipelines.
* **Secure Architecture:** Professional secret management for local `.env` and Cloud deployment.

## 🛠️ Tech Stack
* **Language:** Python 3.12 (Conda Environment)
* **AI Engine:** Google Gemini API (`google-genai` SDK)
* **UI Framework:** Streamlit
* **Data Processing:** Pandas & Regular Expressions

## 📂 Project Structure
```text
synthetic-data-factory/
├── .streamlit/          # Cloud configuration
├── src/
│   ├── __init__.py      # Package initialization
│   └── processor.py     # Data parsing & JSONL logic
├── app.py               # Streamlit UI
├── generator.py         # Gemini API integration
├── requirements.txt     # Dependency list
└── README.md            # Documentation

⚙️ Installation & Setup
Clone the Repository

Bash
git clone [https://github.com/Aakarshkumar612/synthetic-data-factory.git](https://github.com/Aakarshkumar612/synthetic-data-factory.git)
cd synthetic-data-factory
Set Up Environment (Conda)

Bash
conda create -n synthetic_env python=3.12 -y
conda activate synthetic_env
Install Dependencies

Bash
pip install -r requirements.txt
Configure API Keys
Create a .env file in the root directory:

Plaintext
GEMINI_API_KEY=your_actual_api_key_here
🖥️ Usage
Run the application locally:

Bash
streamlit run app.py
Enter your niche topic, choose the number of samples, and download your training-ready dataset!

📄 License
Distributed under the MIT License. See LICENSE for more information.

Developed by Aakarsh Kumar


