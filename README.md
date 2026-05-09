
`markdown

DSN x BCT LLM Agent: Contextual Nigerian Consumer Recommender

![FastAPI](https://fastapi.tiangolo.com/)
![Docker](https://www.docker.com/)
![Groq](https://groq.com/)

---

🇳🇬 Project Overview
This project was built for the DSN x BCT AI Agent Challenge.  
It’s a containerized LLM‑powered agent designed to connect global e‑commerce data with the realities of the Nigerian consumer market.  

Instead of just pattern matching, the agent applies Agentic Reasoning to simulate behavior and make recommendations that reflect:
- Infrastructure challenges (power outages, data costs)
- Cultural context
- Economic considerations

---

🚀 Key Features

Task A: Behavioral User Modeling
- Realistic Simulation: Produces reviews and ratings that sound authentically Nigerian, factoring in things like generator fuel costs, solar needs, and even Pidgin English.
- Persona Projection: Converts purchase history into living consumer profiles (e.g., Emmanuel, 32 from Lagos).

Task B: Contextual Recommendation
- Agentic Reasoning: Assesses products for their usefulness in Nigerian settings (e.g., recommending a kettle as a backup cooking option during blackouts).
- Cross‑Domain Suggestions: Goes beyond products to suggest experiences, like pairing kitchenware with Nigerian staples such as Jollof Rice.

---

🛠️ Architecture & Tech Stack
- Backend: FastAPI (Python 3.12)
- LLM Engine: Llama‑3.3‑70b via Groq Cloud for fast inference
- Data Engine: Pandas for efficient history retrieval
- Deployment: Dockerized and hosted on Render for always‑on API access

---

📦 Local Setup & Deployment

1. Clone the Repository
`bash
git clone https://github.com/donfaruk19/dsn-bct-agent.git
cd dsn-bct-agent
`

2. Configure Environment
Set up your GROQAPIKEY.  
- For local runs, add it to your environment variables.  
- For Docker/Render, configure it through the dashboard.

3. Run via Docker
`bash
docker build -t bct-agent .
docker run -p 8000:8000 bct-agent
`

---

🧪 Sample API Outputs

Task A: Simulate Review
- Endpoint: POST /task-a/simulate  
- Input: Solar Inverter 5KVA  
- Output:  
  > "I must say, dis Solar Inverter 5KVA be game changer for my home in Lagos... e dey perform wonderfully... e dey save me plenty money on diesel for my generator... overall, I rate am 4 star."

Task B: Get Recommendation
- Endpoint: POST /task-b/recommend  
- Input: User Persona (AG3D6O...)  
- Output:  
  > Recommendation: iBELL Multi Purpose Kettle/Cooker  
  > Reasoning: "Nigeria often experiences power outages... this is a reliable alternative for cooking... fits a young, urban individual's lifestyle."  
  > Cross‑Domain: "Pairs perfectly with preparing Jollof Rice."

---

📁 Repository Structure
`text
├── app/
│   ├── main.py          # API Gateway & Endpoints
│   ├── persona.py       # User Modeling Logic (Task A)
│   ├── recommender.py   # Agentic Reasoning Logic (Task B)
│   └── data_utils.py    # Data Pipeline & Token Management
├── amazon.csv           # Source Dataset
├── Dockerfile           # Container Configuration
├── requirements.txt     # Dependencies
└── README.md            # Documentation
`

---

📝 Deliverables
- x] 01 Link to Agent: [https://dsn-bct-agent.onrender.com  
- [x] 02 Solution Paper: 4–8 page technical write‑up (submitted)  
- [x] 03 Code Repository: Clean, modular, and documented  

---

Developed by donfaruk19 for the DSN x BCT AI Agent Hackathon 2026.
`