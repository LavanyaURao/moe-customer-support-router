
#  Smart Customer Support Router (Mixture of Experts - MoE)

## 📌 Project Overview

This project implements a **Mixture of Experts (MoE) architecture** using the Groq API.

Instead of relying on a single general-purpose AI model, this system intelligently routes user queries to specialized “expert” configurations based on intent classification.

The router acts as a gating mechanism that determines which expert should handle a given request.

---

##  Objective

To simulate a real-world customer support system where:

-  **Technical Expert** handles debugging and code-related issues  
-  **Billing Expert** handles refund and payment-related queries  
-  **General Expert** handles casual and fallback queries  
-  **Tool Expert (Bonus)** handles structured tool-based queries like Bitcoin price  

---

##  Architecture

```
User Input
     ↓
Intent Router (temperature = 0)
     ↓
Expert Selection (System Prompt Switching)
     ↓
Specialized LLM (temperature = 0.7)
     ↓
Final Response
```

### Architecture Explanation

- The **Router** performs deterministic classification.
- The **Experts** are simulated using different system prompts.
- The same base model is reused for all experts.
- Tool-based queries bypass the LLM and call a function directly.
- Clean separation between routing and execution logic.

---

##  Technologies Used

- Python
- Groq API
- python-dotenv
- LLaMA 3.1 8B Instant Model

---

##  Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/moe-customer-support-router.git
cd moe-customer-support-router
```

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your Groq API Key

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_api_key_here
```

---

##  Run the Project

```bash
python main.py
```

---

##  Example Test Queries

### Technical Query
```
My Python script is throwing an IndexError on line 5.
```

### Billing Query
```
I was charged twice for my subscription this month.
```

### General Query
```
Tell me a joke.
```

### Tool Query (Bonus)
```
What is the current price of Bitcoin?
```


---


##  Concepts Demonstrated

- Mixture of Experts (MoE)
- Intent Classification
- Prompt Engineering
- Deterministic Routing
- Tool Integration
- Modular AI Architecture
- Separation of Concerns
