# 💻 Coding Helper Chatbot

An AI-powered **Coding Assistant** built using a **Local Large Language Model (Phi-3 Mini)** running on **LM Studio**, with a modular and scalable architecture using **Streamlit**.

This chatbot helps users **learn programming, generate code, and debug errors** — completely **offline without any cloud APIs**.

---

## 🚀 Features

* 💬 **Conversational Coding Assistant**
* 🧠 **Code Generation (Python, Java, C++, JS)**
* 🛠 **Debugging Support**
* 📘 **Concept Explanation**
* ⚡ **Fast Local Responses**
* 🔒 **Fully Offline & Privacy-Focused**
* 🧩 **Modular Code Structure (Industry-style)**

---

## 🏗 Project Structure

```
coding-helper-chatbot/
│
├── app.py              # Main Streamlit application
├── llm_client.py       # Handles LM Studio API calls
├── prompts.py          # System prompt and templates
├── ui.py               # UI components (chat, sidebar)
├── config.py           # Configuration (API, model, params)
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---

## 🧰 Technologies Used

* **Python**
* **Streamlit** – UI framework
* **LM Studio** – Local LLM server
* **Phi-3 Mini (4K Instruct)** – Language Model
* **Requests** – API communication

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Setup LM Studio

1. Download LM Studio: https://lmstudio.ai
2. Open and load model:

```
phi-3-mini-4k-instruct
```

3. Start Local Server:

```
http://127.0.0.1:1234
```

---

### 3️⃣ Run the Application

```bash
python -m streamlit run app.py
```

---

### 4️⃣ Open in Browser

```
http://localhost:8501
```

---

## 🔄 System Workflow

```
User Input (Streamlit UI)
        ↓
Prompt Construction (prompts.py)
        ↓
LLM Client (llm_client.py)
        ↓
LM Studio API (localhost:1234)
        ↓
Phi-3 Model Response
        ↓
UI Display (ui.py)
```

---

## 🧠 Prompt Engineering

The chatbot uses:

* **Role Prompting** → Defines assistant behavior
* **Instruction Prompting** → Guides response structure
* **Constraint Prompting** → Controls output
* **Few-shot Prompting** → Improves response accuracy

---

## 🔒 Privacy & Advantages

* ✅ Runs completely offline
* ✅ No external API calls
* ✅ Faster response time
* ✅ Secure and private

---

## 🧪 Example Queries

* Explain binary search in Java
* Write a Python program for factorial
* Fix this error: IndexError
* Explain sliding window technique
* Show quicksort implementation

---

## ⚠️ Troubleshooting

### ❌ Cannot connect to LM Studio

* Ensure LM Studio is running
* Check server at `http://127.0.0.1:1234`
* Make sure model is loaded

---

### ❌ No response from chatbot

* Check `"model": "phi-3-mini-4k-instruct"` in config.py
* Restart LM Studio

---

### ❌ Streamlit not recognized

```bash
python -m streamlit run app.py
```

---

## 📊 Requirements

* Python 3.8+
* 8 GB RAM (recommended)
* LM Studio installed
* Phi-3 Mini model downloaded

---

## 📄 License

This project is for **educational purposes**.
LM Studio and Phi-3 models follow their respective licenses.

---

## ❤️ Acknowledgement

Built using **Local LLM + Prompt Engineering + Streamlit** to create an efficient offline coding assistant.
