# DSN x BCT LLM Agent: Nigerian Consumer AI Agent

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Groq](https://img.shields.io/badge/Llama_3.3-Groq-orange)](https://groq.com/)

## 🇳🇬 Project Overview
This project was built for the **DSN x BCT AI Agent Challenge**. It is a containerized LLM‑powered agent designed to connect global e‑commerce data with the realities of the Nigerian consumer market.  

Instead of just pattern matching, the agent applies **Agentic Reasoning** to simulate behavior and make recommendations that reflect:
- Infrastructure challenges (power outages, diesel costs)
- Cultural context (Pidgin English, local lifestyle)
- Economic considerations (utility vs. prestige)


## 🚀 Key Features

### Task A: Behavioral User Modeling
- **Realistic Simulation**: Produces reviews and ratings that sound authentically Nigerian, factoring in things like generator fuel costs, solar needs, and Pidgin English.
- **Persona Projection**: Converts purchase history into living consumer profiles (e.g., Emmanuel, 32 from Lagos).

### Task B: Contextual Recommendation
- **Agentic Reasoning**: Assesses products for their usefulness in Nigerian settings (e.g., recommending a kettle as a backup cooking option during blackouts).
- **Cross‑Domain Suggestions**: Suggests local experiences, like pairing kitchenware with Nigerian staples such as Jollof Rice.


## 🛠️ Architecture & Tech Stack
- **Backend**: FastAPI (Python 3.12)
- **LLM Engine**: Llama‑3.3‑70b via Groq Cloud for fast inference
- **Data Engine**: Pandas for efficient history retrieval
- **Deployment**: Dockerized and hosted on Render for always‑on API access


## 📦 Setup & Deployment

### 1. Clone the Repository
```bash
git clone [https://github.com/donfaruk19/dsn-bct-agent.git](https://github.com/donfaruk19/dsn-bct-agent.git)
cd dsn-bct-agent

```
### 2. Configure Environment
Create a .env file or export your API key:
 * GROQ_API_KEY=your_gsk_key_here
### 3. Run via Docker
```bash
docker build -t bct-agent .
docker run -p 8000:8000 --env-file .env bct-agent

```
## 🧪 Testing the API
You can test the agent in any environment (Local, Docker, or the Live Render URL) using the commands below.
> **Note:** To test the Live version, replace http://127.0.0.1:8000 with https://dsn-bct-agent.onrender.com
> 
### Test Task A: Simulate Review
```bash
curl -X POST "[http://127.0.0.1:8000/task-a/simulate](http://127.0.0.1:8000/task-a/simulate)" \
     -H "Content-Type: application/json" \
     -d '{
          "user_id": "AG3D6O4STAQKAY2UVGEUV46KN35Q", 
          "product_name": "Solar Inverter 5KVA", 
          "product_description": "Pure sine wave inverter for Nigerian homes."
         }'

```
### Test Task B: Contextual Recommendation
```bash
curl -X POST "[http://127.0.0.1:8000/task-b/recommend](http://127.0.0.1:8000/task-b/recommend)" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "AG3D6O4STAQKAY2UVGEUV46KN35Q"}'

```
## 📁 Repository Structure
```text
├── app/
│   ├── main.py          # API Gateway & Endpoints
│   ├── persona.py       # User Modeling Logic (Task A)
│   ├── recommender.py   # Agentic Reasoning Logic (Task B)
│   └── data_utils.py    # Data Pipeline & Token Management
├── amazon.csv           # Source Dataset
├── Dockerfile           # Container Configuration
├── requirements.txt     # Dependencies
└── README.md            # Documentation

```
## 📝 Deliverables
 * [x] **01 Link to Agent:** https://dsn-bct-agent.onrender.com
 
**Developed by donfaruk19 for the DSN x BCT AI Agent Hackathon 2026.**