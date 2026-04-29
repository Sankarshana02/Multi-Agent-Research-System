# 🤖 OdinAI — Multi-Agent AI Research System


> 🧠 An intelligent multi-agent system that autonomously searches, analyzes, and generates structured research reports.

---

## 🚀 Overview
**OdinAI** is a multi-agent AI system inspired by **Odin**, the Norse god of wisdom, knowledge, and foresight.  
Just like Odin sought knowledge from all realms, this system gathers and synthesizes information using multiple AI agents.
It simulates collaborative intelligence using multiple specialized agents.

✨ It performs:
- 🔍 Web search (Tavily)
- 📄 Content extraction (BeautifulSoup)
- 🧠 Structured report generation (Mistral LLM)
- 🧾 Critical evaluation of outputs

All wrapped in a Streamlit UI with:
- 📐 LaTeX equation rendering  
- 📊 Markdown tables  
- 🎨 Clean UI  

---

## 🧠 Architecture

User Input  
↓  
🔍 Search Agent  
↓  
📄 Reader Agent  
↓  
✍️ Writer Agent  
↓  
🧠 Critic Agent  
↓  
📊 Final Report + Feedback  

---

## ⚙️ Tech Stack

- 🤖 LLM: Mistral (`langchain-mistralai`)  
- 🧩 Framework: LangChain  
- 🔍 Search API: Tavily  
- 🌐 Web Scraping: BeautifulSoup + Requests  
- 🎨 Frontend/UI: Streamlit  

---

## 📂 Project Structure

```
argus-ai/
├── app.py
├── pipeline.py
├── agents.py
├── tools.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup (Local)

### 1. Clone the repo
```
git clone https://github.com/your-username/argus-ai.git
cd argus-ai
```

### 2. Create virtual environment
```
python -m venv venv
source venv/bin/activate
```

Windows:
```
venv\Scripts\activate
```

---

### 3. Install dependencies
```
pip install -r requirements.txt
```

---

### 4. Add environment variables

Create a `.env` file:

```
MISTRAL_API_KEY=your_mistral_key
TAVILY_API_KEY=your_tavily_key
```

---

### 5. Run the app
```
streamlit run app.py
```

---
## ✨ Features

- 🤖 Multi-agent collaboration  
- 🔍 Real-time web search  
- 📄 Intelligent content extraction  
- ✍️ Structured report generation  
- 🧠 Automated critique and scoring  
- 📊 Proper table rendering  
- 📐 LaTeX equation support  
- 🎨 Clean UI  

---

## 🔮 Future Improvements

- 📄 PDF export  
- ⚡ Streaming responses  
- 📊 Interactive tables  
- 🌐 Custom domain deployment  
- 🧠 Memory-enabled agents  
- 🔄 LangGraph integration  



## 💬 Author

Built with ❤️ as a multi-agent AI research system.

---

## 🚀 Live Demo

👉 [OdinAI](https://odinai.streamlit.app/)
