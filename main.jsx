import React from 'react'
import ReactDOM from 'react-dom/client'

const App = () => (
  <div style={{
    height: '100vh',
    backgroundColor: 'black',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    color: 'white',
    fontSize: '2rem'
  }}>
    Trust is the New Compute — Recon.AI
  </div>
)

ReactDOM.createRoot(document.getElementById('root')).render(<App />)
