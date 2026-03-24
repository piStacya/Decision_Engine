import { useState } from "react";
import LoanForm from "./components/LoanForm";
import LoanResult from "./components/LoanResult";
import "./App.css";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="app">
      <h1>Inbank Loan Decision Engine</h1>
      <LoanForm onResult={setResult} />
      {result && <LoanResult result={result} />}
    </div>
  );
}

export default App;
