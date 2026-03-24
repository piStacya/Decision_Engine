CREDIT_PROFILES = {
    "49002010965": {"debt": True},
    "49002010976": {"debt": False, "credit_modifier": 100},
    "49002010987": {"debt": False, "credit_modifier": 300},
    "49002010998": {"debt": False, "credit_modifier": 1000},
}

MIN_AMOUNT = 2000
MAX_AMOUNT = 10000
MIN_PERIOD = 12
MAX_PERIOD = 60


def calculate_credit_score(credit_modifier: int, loan_amount: float, loan_period: int) -> float:
    return (credit_modifier / loan_amount) * loan_period


def get_maximum_approved_amount(credit_modifier: int, loan_period: int) -> float:
    max_amount = credit_modifier * loan_period
    return min(max_amount, MAX_AMOUNT)


def make_decision(personal_code: str, loan_amount: float, loan_period: int) -> dict:
    if personal_code not in CREDIT_PROFILES:
        return {
            "decision": "negative",
            "approved_amount": 0,
            "approved_period": loan_period,
            "message": "Unknown personal code.",
        }

    profile = CREDIT_PROFILES[personal_code]

    if profile["debt"]:
        return {
            "decision": "negative",
            "approved_amount": 0,
            "approved_period": loan_period,
            "message": "Loan denied due to existing debt.",
        }

    credit_modifier = profile["credit_modifier"]

    # leian suurima lubatud amounti selleks perioodiks
    approved_amount = get_maximum_approved_amount(credit_modifier, loan_period)

    if approved_amount >= MIN_AMOUNT:
        return {
            "decision": "positive",
            "approved_amount": approved_amount,
            "approved_period": loan_period,
            "message": f"Approved for €{approved_amount:.0f} over {loan_period} months.",
        }

    # kui pole võimalik küsitud perioodiks, siis proovin suurendada perioodi (pikendades seda kuu kaupa kuni max kuude arvuni)
    for period in range(loan_period + 1, MAX_PERIOD + 1):
        approved_amount = get_maximum_approved_amount(credit_modifier, period)
        if approved_amount >= MIN_AMOUNT:
            return {
                "decision": "positive",
                "approved_amount": approved_amount,
                "approved_period": period,
                "message": f"Approved for €{approved_amount:.0f} over {period} months.",
            }

    return { # kui ükski eelnevatest ei läinud läbi, siis keeldun (isegi 60 kuuga ei saa 2000 kokku)
        "decision": "negative",
        "approved_amount": 0,
        "approved_period": loan_period,
        "message": "No suitable loan amount found within allowed constraints.",
    }
