# LangChain Streamlit Chatbot with Ollama & LangSmith

## 🚀 Overview

This project is a conversational AI chatbot built using **LangChain**, **Streamlit**, and **Ollama**. It enables users to interact with a locally hosted Large Language Model (LLM) through a simple web interface while leveraging **LangSmith** for monitoring, tracing, and debugging chain executions.

The application demonstrates how to integrate modern AI orchestration frameworks with local LLMs, making it suitable for learning, experimentation, and building production-ready AI applications.

---

## ✨ Features

* Interactive chatbot interface built with Streamlit
* Local LLM inference using Ollama (Llama 2)
* Prompt engineering using LangChain Prompt Templates
* Structured output handling with LangChain Output Parsers
* LangSmith integration for tracing and debugging
* Environment variable management using python-dotenv
* Lightweight and easy to deploy
* Privacy-friendly local model execution

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Ollama
* LangSmith
* Llama 2
* Python Dotenv

---

## 📂 Project Structure

```text
.
├── app.py
├── .env
├── requirements.txt
├── README.md
└── assets/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/langchain-streamlit-chatbot.git
cd langchain-streamlit-chatbot
```

### 2. Create Conda Environment

```bash
ocnda create -n venv python=3.10
```

Activate the environment:

**Windows**

```bash
conda actiavte venv
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the Llama 2 model:

```bash
ollama pull llama2
```

Verify the model:

```bash
ollama list
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=TestProject
LANGCHAIN_TRACING_V2=true
```

---

## ▶️ Run the Application

Start Ollama:

```bash
ollama serve
```

Launch the Streamlit application:

```bash
streamlit run app.py
```

Open your browser and navigate to:

```text
http://localhost:8501
```

---

## 🧠 How It Works

1. User enters a question in the Streamlit interface.
2. LangChain constructs a prompt using a predefined template.
3. The prompt is sent to the local Llama 2 model via Ollama.
4. The model generates a response.
5. LangChain parses and returns the output.
6. LangSmith captures traces for debugging and monitoring.

---

## 📊 LangSmith Monitoring

This project supports LangSmith tracing to:

* Monitor chain execution
* Debug prompt flows
* Analyze model responses
* Track application performance
* Improve prompt engineering workflows

---

## 📸 Demo

Example Query:

```text
What is Machine Learning?
```

Example Response:

```text
Machine Learning is a subset of Artificial Intelligence that enables systems to learn patterns from data and improve performance without being explicitly programmed.
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

## 👨‍💻 Author

**Ambesh Mishra**
LinkedIn: https://linkedin.com/in/ambesh-mishra

**Output:**
<img width="1909" height="826" alt="image" src="https://github.com/user-attachments/assets/74d8f278-f723-4f15-9695-8c4335b0c35a" />
<img width="1899" height="893" alt="image" src="https://github.com/user-attachments/assets/3994a186-021c-4719-86be-b29f2214642e" />


