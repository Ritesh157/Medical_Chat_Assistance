# Medical ChatBot Assistance

MediChat Pro is an innovative medical chatbot assistant designed to help users interpret and extract insights from medical reports in PDF format. Powered by advanced language models and a vector database, MediChat Pro enables users to upload their medical reports and engage in natural, conversational queries to understand their health data better. Built with Streamlit for a seamless frontend and leveraging FAISS Vector DB and HuggingFaceEmbeddings, MediChat Pro provides accurate and context-aware responses.

## ✨ Features

- PDF Report Upload: Upload medical reports in PDF format for analysis.
- Conversational Insights: Chat with the assistant to extract specific details or explanations from your report.
- Context-Aware Responses: Powered by sentence-transformers/all-mpnet-base-v2 for precise embeddings and FAISS for efficient retrieval.
- User-Friendly Interface: Streamlit-based frontend for a smooth and intuitive user experience.
- Scalable and Fast: Optimized for quick processing of medical reports using vector search.

## 🛠️ Installation

Get MediChat Pro up and running in just a few steps:

- Python: 3.10
- Streamlit: For the frontend interface
- FAISS: Vector database for efficient similarity search
- HuggingFace Transformers: For embeddings (sentence-transformers/all-mpnet-base-v2)
- Other dependencies listed in requirements.txt


## Steps

Clone the repository:

```sh
bash
https://github.com/Ritesh157/Medical_Chat_Assistance.git
```
Navigate to the project directory:

```sh
bash
cd Medical_Chat_Assistance
```
Create a virtual environment (optional but recommended):
```sh
bash
conda create -n medichatpro python=3.10
```
Activate virtual environment:
```sh
bash
conda activate medichatpro
```
Install dependencies:
```sh
bash
pip install -r requirements.txt
```
Run the Streamlit app:
```sh
bash
streamlit run main.py
```
## 🚀 Usage

- Launch the Streamlit app by running the command above
- Upload your medical report in PDF format through the web interface (You can upload multiple files).
- Start chatting with MediChat Pro to ask questions about your report.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.