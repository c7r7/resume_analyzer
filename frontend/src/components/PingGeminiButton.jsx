import { useState } from 'react'
import { pingGemini } from '../api/geminiApi'

function PingGeminiButton() {
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)

  const handlePing = async () => {
    setLoading(true)
    setError(null)
    setResult(null)
    try {
      setResult(await pingGemini())
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <button onClick={handlePing} disabled={loading}>
        {loading ? 'Pinging Gemini...' : 'Ping Gemini'}
      </button>
      {result && <p className="result">{result}</p>}
      {error && <p className="error">Error: {error}</p>}
    </>
  )
}

export default PingGeminiButton
