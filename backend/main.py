from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cambiamos la ruta a /api/profile
@app.get("/api/profile")
def get_profile():
    return {
        "nombre": "Sergio Rodríguez Quintana",
        "titular": "Junior Cloud & DevOps / Operaciones",
        "formacion": "Técnico Superior en Administración de Sistemas Informáticos en Red (ASIR)",
        "perfil": "Perfil orientado a Cloud/DevOps, con gran interés en automatización, infraestructura moderna y mejora continua.",
        "tecnologias": [
            "Microsoft Azure", 
            "Kubernetes", 
            "CI/CD Pipelines", 
            "Docker", 
            "Python", 
            "Vue.js"
        ],
        "experiencia": [
            {
                "puesto": "Operaciones IT (Proyecto con empresa puntera de España)",
                "empresa": "Viewnext",
                "fecha": "Practicas desde el 2 de Febrero e Incorporación desde el 15 de Junio",
                "descripcion": "Despliegues, troubleshooting y soporte de aplicaciones en entornos contenerizados."
            }
        ],
        "intereses": [
            "Juegos de mesa"
            "Fútbol español (UD Almería, Real Betis, RCD Mallorca)",
            "Música en streaming (Natos y Waor, Reality, Marea, Extremoduro)"
        ]
    }