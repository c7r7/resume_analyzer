export async function pingGemini() {
  const res = await fetch('/api/ping-gemini')
  const data = await res.json()
  if (!res.ok) {
    throw new Error(data.detail || `Request failed with status ${res.status}`)
  }
  return data.response
}
