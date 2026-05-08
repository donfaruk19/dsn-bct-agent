```markdown
# DSN x BCT LLM Agent: Contextual Nigerian Consumer Recommender

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Groq](https://img.shields.io/badge/Llama_3.3-Groq-orange)](https://groq.com/)

## 🇳🇬 Project Overview
This repository contains a containerized LLM-based agent developed for the **DSN X BCT AI Agent Challenge**. The agent is engineered to bridge the gap between global e-commerce data and the unique Nigerian consumer landscape. 

Instead of basic pattern matching, this agent uses **Agentic Reasoning** to simulate user behavior and recommend products based on local infrastructure constraints (power, data), cultural nuances, and economic factors.

---

## 🚀 Key Features

### Task A: Behavioral User Modeling
- **High-Fidelity Simulation**: Generates star ratings and reviews that capture the specific "Nigerian voice," including local context (Diesel/Gen costs, Solar needs) and linguistic nuances (Pidgin English).
- **Persona Projection**: Transforms static purchase history into a dynamic consumer profile (e.g., "Emmanuel, 32 from Lagos").

### Task B: Contextual Recommendation
- **Agentic Reasoning**: Evaluates products based on utility in the Nigerian environment (e.g., recommending a multi-purpose kettle as a reliable cooking alternative during power outages).
- **Cross-Domain Retrieval**: Suggests complementary local experiences, such as pairing technology/kitchenware with Nigerian cuisine like **Jollof Rice**.

---

## 🛠️ Architecture & Tech Stack
- **Backend**: FastAPI (Python 3.12)
- **LLM Engine**: Llama-3.3-70b via **Groq Cloud** for low-latency inference.
- **Data Engine**: Pandas for optimized history retrieval.
- **Deployment**: Dockerized and hosted on **Render** for 24/7 API availability.

---

## 📦 Local Setup & Deployment

### 1. Clone the Repository
```bash
git clone [https://github.com/donfaruk19/dsn-bct-agent.git](https://github.com/donfaruk19/dsn-bct-agent.git)
cd dsn-bct-agent

```

### 2. Configure Environment

The application requires a `GROQ_API_KEY`. For local runs, add it to your environment variables. For Docker/Render, it is configured via the dashboard.

### 3. Run via Docker

```bash
docker build -t bct-agent .
docker run -p 8000:8000 bct-agent

```

---

## 🧪 Verified API Outputs (Live Tests)

### Task A: Simulate Review

**Endpoint:** `POST /task-a/simulate`
**Input:** Solar Inverter 5KVA
**Agent Output:** > *"I must say, dis Solar Inverter 5KVA be game changer for my home in Lagos... e dey perform wonderfully... e dey save me plenty money on diesel for my generator... overall, I rate am 4 star."*

### Task B: Get Recommendation

**Endpoint:** `POST /task-b/recommend`
**Input:** User Persona (AG3D6O...)
**Agent Output:**

> **Recommendation:** iBELL Multi Purpose Kettle/Cooker.
> **Reasoning:** *"Nigeria often experiences power outages... this is a reliable alternative for cooking... fits a young, urban individual's lifestyle."*
> **Cross-Domain:** *"Pairs perfectly with preparing Jollof Rice."*

---

## 📁 Repository Structure

```text
├── app/
│   ├── main.py          # API Gateway & Endpoints
│   ├── persona.py       # User Modeling Logic (Task A)
│   ├── recommender.py   # Agentic Reasoning Logic (Task B)
│   └── data_utils.py    # Data Pipeline & Token Management
├── amazon.csv           # Source Dataset
├── Dockerfile           # Optimized Container Configuration
├── requirements.txt     # Dependency Manifest
└── README.md            # Documentation

```

---

## 📝 Deliverables Status

* [x] **Link to Agent:** [https://dsn-bct-agent.onrender.com](https://dsn-bct-agent.onrender.com)

**Developed by donfaruk19 for the DSN X BCT AI Agent Hackathon 2026.**

```

```
