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
            "Me encanta viajar",
            "Amante de los juegos de mesa y tiempo con amigos",
            "Tecnología: Automatización de infraestructura y cultura DevOps.",
            "Deportes: Seguidor de la UD Almería, Snowboard, Crossfit, Padel.",
            "Música: Marea, Extremoduro, Natos y Waor, Reality."
        ],
        "proyectos": [
            {
                "nombre": "Infraestructura Cloud & Homelab",
                "descripcion": "Diseño, despliegue y administración de un servidor VPS en IONOS (Linux M) con Kubernetes. Incluye Ingress Traefik, monitorización mediante Grafana, Prometheus y Loki, y un sistema de alertas de seguridad automatizado con un bot de Telegram.",
                "tecnologias": ["Kubernetes", "Traefik", "Grafana", "Loki", "IONOS VPS"]
            },
            {
                "nombre": "Pipeline CI/CD & GitOps",
                "descripcion": "Despliegue automatizado del portfolio aplicando filosofía GitOps con GitHub Actions. Contenedores Dockerizados, versionado semántico por commit SHA y actualizaciones sin cortes de servicio (Zero-Downtime deployments).",
                "tecnologias": ["GitHub Actions", "Docker", "Python", "YAML"]
            },
            {
                "nombre": "Sistema de Backups Automatizado",
                "descripcion": "Implementación de copias de seguridad automatizadas en la nube utilizando Google Drive para salvaguardar los datos críticos del servidor y los manifiestos de la infraestructura, asegurando la recuperación ante desastres.",
                "tecnologias": ["Bash", "Cron", "Google Drive API", "Linux"]
            }
        ],
        "contacto": {
            "email_user": "sergiomack91",
            "email_domain": "gmail.com",
            "github": "https://github.com/Sergiomack91",
            "linkedin": "https://www.linkedin.com/in/sergio-rodr%C3%ADguez-quintana-28bbb02a3/"
        }

    }