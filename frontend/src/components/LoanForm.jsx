// vorm kolme väljaga: isikukood, summa, periood
import { useState } from "react";

const MIN_AMOUNT = 2000;
const MAX_AMOUNT = 10000;
const MIN_PERIOD = 12;
const MAX_PERIOD = 60;

function LoanForm({ onResult }) {
  const [personalCode, setPersonalCode] = useState("");
  const [loanAmount, setLoanAmount] = useState(5000);
  const [loanPeriod, setLoanPeriod] = useState(36);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await fetch("http://localhost:8000/api/loan/decision", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          personal_code: personalCode,
          loan_amount: loanAmount,
          loan_period: loanPeriod,
        }),
      });

      if (!response.ok) {
        throw new Error("Invalid input or server error.");
      }

      const data = await response.json();
      onResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <form className="loan-form" onSubmit={handleSubmit}>
      <div className="field">
        <label>Personal Code</label>
        <input
          type="text"
          value={personalCode}
          onChange={(e) => setPersonalCode(e.target.value)}
          placeholder="e.g. 12345678910"
          requireds
        />
      </div>

      <div className="field">
        <label>Loan Amount: €{loanAmount}</label>
        <input
          type="range"
          min={MIN_AMOUNT}
          max={MAX_AMOUNT}
          step={100}
          value={loanAmount}
          onChange={(e) => setLoanAmount(Number(e.target.value))}
        />
        <div className="range-labels">
          <span>€{MIN_AMOUNT}</span>
          <span>€{MAX_AMOUNT}</span>
        </div>
      </div>

      <div className="field">
        <label>Loan Period: {loanPeriod} months</label>
        <input
          type="range"
          min={MIN_PERIOD}
          max={MAX_PERIOD}
          step={1}
          value={loanPeriod}
          onChange={(e) => setLoanPeriod(Number(e.target.value))}
        />
        <div className="range-labels">
          <span>{MIN_PERIOD} months</span>
          <span>{MAX_PERIOD} months</span>
        </div>
      </div>

      {error && <p className="error">{error}</p>}

      <button type="submit" disabled={loading}>
        {loading ? "Calculating..." : "Get Decision"}
      </button>
    </form>
  );
}

export default LoanForm;
