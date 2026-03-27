# 🚀 Agentic AI on Minikube

---

# 📘 Agents Overview

## 🤖 Agent Bot

* Simple linear flow: `START → LLM → END`
* Stateless (no memory)


---

## 🧠 Memory Agent

* Maintains conversation history per session
* Uses in-memory session store


---

## 🔄 ReAct Agent

* Uses tools (add, subtract, multiply)
* Iterative reasoning until no tool calls remain


---

## ✍️ Drafter Agent

* Document creation and editing
* Supports:

  * update document
  * save document

---

## 📚 RAG Agent

* Retrieval-Augmented Generation
* Uses PDF + ChromaDB vector store

---

# 🏗️ Project Structure

```
.
├── Agents/
│   ├── Agent_Bot.py
│   ├── Memory_Agent.py
│   ├── ReAct.py
│   ├── Drafter.py
│   ├── RAG_Agent.py
│   └── data (chroma + pdf)
├── app/
│   └── main.py
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# ⚙️ Setup Instructions

## 1. Start Minikube

```
minikube start
```

---

## 2. Build Docker Image

```
docker build -t agentic-ai:v1 .
minikube image load agentic-ai:v1
```

---

## 3. Deploy to Kubernetes

```
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

---

## 4. Port Forward

```
kubectl port-forward svc/agentic-ai-service 8080:8000
```

---

# 🔑 Environment Variables

## OpenAI (Paid)

```
OPENAI_API_KEY=your-key
```

## OR Gemini (Free - Recommended for Testing)

```
GOOGLE_API_KEY=your-key
```

---

# 🧪 API Testing

## Agent Bot

```
curl -X POST http://localhost:8080/api/agent-bot/chat \
-H "Content-Type: application/json" \
-d '{"message": "What is LangGraph?"}'
```

---

## Memory Agent

```
curl -X POST http://localhost:8080/api/memory/chat \
-H "Content-Type: application/json" \
-d '{"session_id": "user1", "message": "My name is Saurabh"}'
```

---

## ReAct Agent

```
curl -X POST http://localhost:8080/api/react/chat \
-H "Content-Type: application/json" \
-d '{"message": "Add 10 and 20"}'
```

---

## Drafter Agent

```
curl -X POST http://localhost:8080/api/drafter/chat \
-H "Content-Type: application/json" \
-d '{"session_id": "doc1", "message": "Create a document about Kubernetes"}'
```

---

## RAG Agent

```
curl -X POST http://localhost:8080/api/rag/chat \
-H "Content-Type: application/json" \
-d '{"message": "Summarize stock market performance"}'
```

---

# ❤️ Health Check

```
curl http://localhost:8080/health
```

---

Screenshots :

<img width="1864" height="1070" alt="image" src="https://github.com/user-attachments/assets/93c8586c-404c-4c23-a52f-e8547258cbd7" />
<img width="1864" height="1070" alt="image" src="https://github.com/user-attachments/assets/64cdd10e-0e67-4246-b7ee-908348987c2a" />
<img width="1864" height="1070" alt="image" src="https://github.com/user-attachments/assets/e0e9290a-f0ac-4e17-8713-1e2465170cd8" />



---
