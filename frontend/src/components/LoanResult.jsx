// kuvab vastuse
function LoanResult({ result }) {
  const isPositive = result.decision === "positive";

  return (
    <div className={`result ${isPositive ? "positive" : "negative"}`}>
      <h2>{isPositive ? "Approved" : "Denied"}</h2>
      <p>{result.message}</p>
      {isPositive && (
        <div className="result-details">
          <div className="detail">
            <span>Amount</span>
            <strong>€{result.approved_amount.toLocaleString()}</strong>
          </div>
          <div className="detail">
            <span>Period</span>
            <strong>{result.approved_period} months</strong>
          </div>
        </div>
      )}
    </div>
  );
}

export default LoanResult;
