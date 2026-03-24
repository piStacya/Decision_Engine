from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import LoanRequest, LoanResponse
from decision_engine import make_decision

app = FastAPI(title="Inbank Decision Engine") # loon rakenduse

app.add_middleware(
    CORSMiddleware, # see lubab frontendil backendiga suhelda
    allow_origins=["http://localhost:5173"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

# siin põhimõtteliselt post /api/loan/decision võtab LoanRequesti sisse, kutsub funkt. make_decision ja tagastab juba loanresponsi.
@app.post("/api/loan/decision", response_model=LoanResponse) # defineerin endpointi
def loan_decision(request: LoanRequest):
    result = make_decision(
        personal_code=request.personal_code,
        loan_amount=request.loan_amount,
        loan_period=request.loan_period,
    )
    return result
