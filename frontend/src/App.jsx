import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [resumes, setResumes] = useState([])

  useEffect(() => {
    // Fetch ผ่าน /api ซึ่ง Caddy จะ Route ไปหา Backend ให้
    fetch('/api/resumes/') 
      .then(res => res.json())
      .then(data => setResumes(data))
  }, [])

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6 text-center text-blue-600">Resume Hub test</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {resumes.map(resume => (
          <div key={resume.id} className="bg-white p-6 rounded-lg shadow-lg hover:shadow-xl transition">
            <h2 className="text-xl font-bold">{resume.title}</h2>
            <p className="text-gray-600">{resume.summary}</p>
            <div className="mt-4 flex flex-wrap gap-2">
                {resume.skills.map(skill => (
                  <span key={skill.name} className="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded">{skill.name}</span>
                ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
export default App
