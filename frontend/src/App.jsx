import { useState } from 'react'
import './App.css'

function App() {
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)

  const pingGemini = async () => {
    setLoading(true)
    setError(null)
    setResult(null)
    try {
      const res = await fetch('/api/ping-gemini')
      const data = await res.json()
      if (!res.ok) {
        throw new Error(data.detail || `Request failed with status ${res.status}`)
      }
      setResult(data.response)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="container">
      <h1>Resume Analyzer</h1>
      <p>Check that frontend, backend, and Gemini are wired together.</p>
      <button onClick={pingGemini} disabled={loading}>
        {loading ? 'Pinging Gemini...' : 'Ping Gemini'}
      </button>
      {result && <p className="result">{result}</p>}
      {error && <p className="error">Error: {error}</p>}
    </main>
  )
}

export default App
