import './App.css'
import PingGeminiButton from './components/PingGeminiButton'

function App() {
  return (
    <main className="container">
      <h1>Resume Analyzer</h1>
      <p>Check that frontend, backend, and Gemini are wired together.</p>
      <PingGeminiButton />
    </main>
  )
}

export default App
