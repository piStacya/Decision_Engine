from pydantic import BaseModel, Field


class LoanRequest(BaseModel):
    personal_code: str
    loan_amount: float = Field(ge=2000, le=10000)
    loan_period: int = Field(ge=12, le=60)


class LoanResponse(BaseModel):
    decision: str
    approved_amount: float
    approved_period: int
    message: str
