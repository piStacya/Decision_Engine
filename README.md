# Inbank Decision Engine

A loan decision engine that evaluates loan applications and returns the maximum approvable amount based on a credit scoring algorithm.

## How It Works

The engine takes a personal code, loan amount, and loan period as input. Rather than simply approving or denying the requested amount, it always tries to find the **maximum sum it can approve**. If the requested amount is too high, it returns the highest possible amount. If no suitable amount can be found within the requested period, it automatically tries extending the period up to the allowed maximum.

### Credit Score Formula

```
credit_score = (credit_modifier / loan_amount) * loan_period
```

- `score >= 1` → approved
- `score < 1` → not approved

The maximum approvable amount for a given period is derived from this formula by solving for `loan_amount` when `score = 1`:

```
max_amount = credit_modifier * loan_period  (capped at €10,000)
```

### Constraints

| Parameter | Min | Max |
|---|---|---|
| Loan amount | €2,000 | €10,000 |
| Loan period | 12 months | 60 months |

---

## Tech Stack

**Backend:** Python + FastAPI
**Frontend:** React + Vite

The backend and frontend are intentionally separated.

**Why FastAPI:**
FastAPI is modern, fast, and has built-in support for request/response validation via Pydantic. It also auto-generates interactive API documentation (`/docs`) which made manual testing during development straightforward...

**Why Pydantic models (`models.py`):**
Instead of manually validating inputs in the endpoint logic, Pydantic handles this declaratively. If a request comes in with for example loan_amount: 500, FastAPI automatically rejects it with a clear error, no extra code needed. In the end i used sliders for numbers, so that user cannot choose invalid inputs, but still, the inputs can be sent straight forward from curl or postman, and the models.py prevents program crush and mistakes even in this kind of situation...

**Why React + Vite:**
React is the industry standard for building interactive UIs. And Vite provides a fast development server with hot module replacement. For this scope, it keeps the frontend simple and focused on the core functionality.

Also the reason for choosing this technologis is because i had experience with them before.

---

## Running the Project

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

API runs at `http://localhost:8000`

### Frontend

```bash
cd ..
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`

---

### Test personal codes

| Personal code | Profile |
|---|---|
| 49002010965 | Debt — always denied |
| 49002010976 | Segment 1 (credit_modifier = 100) |
| 49002010987 | Segment 2 (credit_modifier = 300) |
| 49002010998 | Segment 3 (credit_modifier = 1000) |

---

## What I Would Improve About the Assignment

The assignment doesn't specify what format the personal code should be or whether it needs to be validated. Right now any string passes through, which is not ideal unvalidated text inputs can be misused with unexpected values. Since we're dealing with Estonian personal codes, it would make sense to at least check that the input is 11 digits, which is the standard format. But actually, there is not much that I can say about improving the assignment, because it was good.
I personally really liked the assignment. There is actually a lot I would love to add here, more complex functionality, that would make this program really usable. Also I liked that there were no limitations for techical choices, thanks to that it was really interesting to develop and make reasonable choices myself.