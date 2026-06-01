from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/profile")
def get_profile():
    return {
        "nombre": "Sergio Rodríguez Quintana",
        "titular": "Junior Cloud & DevOps Engineer | Operaciones IT",
        "sobre_mi": "Profesional junior de Operaciones con formación en Administración de Sistemas Informáticos en Red (ASIR) y experiencia en entornos cloud corporativos. Perfil orientado a Cloud/DevOps, con interés en automatización, infraestructura moderna y mejora continua.",
        "experiencia": [
            {
                "puesto": "Operaciones IT (Proyecto en empresa importante)",
                "empresa": "Viewnext",
                "fecha": "Junio 2026 - Presente",
                "descripcion": "Participación en proyectos con Microsoft Azure, Kubernetes y procesos CI/CD. Colaboración en despliegues, troubleshooting y soporte de aplicaciones en entornos contenerizados."
            },
            {
                "puesto": "Prácticas de Operaciones IT",
                "empresa": "Viewnext",
                "fecha": "Febrero 2026 - Mayo 2026",
                "descripcion": "Prácticas formativas en operaciones, soporte y toma de contacto directa con entornos corporativos reales."
            }
        ],
        "educacion": [
            {
                "titulo": "Administración de Sistemas Informáticos en Red (ASIR)",
                "institucion": "Formación Profesional de Grado Superior",
                "fecha": "Finalizado"
            }
        ],
        "skills": [
            "Microsoft Azure", 
            "Kubernetes", 
            "Docker",
            "CI/CD Pipelines", 
            "Python", 
            "Vue.js",
            "Troubleshooting"
        ],
        "intereses": [
            "Amante de los juegos de mesa",
            "Tecnología: Automatización de infraestructura y cultura DevOps.",
            "Deportes: Seguidor de la UD Almería, Snowboard, Crossfit, Padel.",
            "Música: Natos y Waor, Reality."
        ]
    }