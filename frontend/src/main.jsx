// ühendab reacti html-iga
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

// põhimõtteliselt see käivitab rakenduse ja ütleb pane react komponent sellesse htmli
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
