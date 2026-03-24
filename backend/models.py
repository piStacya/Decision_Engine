from pydantic import BaseModel, Field

# siin defineerin andmete kuju ja reeglid - mis välju ma ootan ja millised väärtused üldse lubatud on
# see on lihtsam lahendus kui hakata pärast main.py-s käsitsi kõike kontrollima
# sest pydantic basemodeliga teeb fastapi seda kõike automaatselt. valed väärtused = ei.
class LoanRequest(BaseModel):
    personal_code: str
    loan_amount: float = Field(ge=2000, le=10000)
    loan_period: int = Field(ge=12, le=60)


class LoanResponse(BaseModel):
    decision: str
    approved_amount: float
    approved_period: int
    message: str
