from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware # IMPORTANTE AÑADIR ESTO
from pydantic import BaseModel
import requests
import os
import sys

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://pruebasergio.com", 
        "https://www.pruebasergio.com",
        "http://localhost:8080",
        "http://localhost:8081"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class CaptchaVerification(BaseModel):
    token: str
@app.post("/api/download-cv")
def download_cv(req: CaptchaVerification):
    secret_key = os.getenv("RECAPTCHA_SECRET_KEY")
    
    if not secret_key:
        raise HTTPException(status_code=500, detail="Error de configuración del servidor")

    verify_url = "https://www.google.com/recaptcha/api/siteverify"
    payload = {"secret": secret_key, "response": req.token}
    response = requests.post(verify_url, data=payload).json()
    
    # Verificamos que la petición sea exitosa y el score sea mayor o igual a 0.5
    if response.get("success") and response.get("score", 0) >= 0.5:
        return FileResponse("cv_sergio_rodriguez.pdf", media_type="application/pdf", filename="cv_sergio_rodriguez.pdf")
    else:
        raise HTTPException(status_code=400, detail="Tráfico sospechoso detectado")

@app.get("/api/profile")
def get_profile():
    return {
        "nombre": "Sergio Rodríguez Quintana",
        "titular": "Operaciones Cloud | Kubernetes & CI/CD | Orientación SRE",
        "sobre_mi": "Profesional de Operaciones IT con formación en Administración de Sistemas Informáticos en Red (ASIR) y experiencia en entornos corporativos. Trabajo con Kubernetes, análisis de logs, CI/CD en Azure DevOps, Python y soporte de aplicaciones .NET y Vue. También utilizo ServiceNow para la gestión operativa y, cuando falta el focal point, apoyo en la coordinación del equipo y el seguimiento de tareas. Me interesa seguir creciendo hacia SRE, con foco en confiabilidad, observabilidad y automatización.",
        "experiencia": [
            {
                "puesto": "Operaciones IT (Proyecto Repsol)",
                "empresa": "Viewnext",
                "fecha": "Febrero 2026 - Presente",
                "descripcion": "Incorporación al proyecto en febrero de 2026 mediante prácticas formativas y continuidad en el equipo de operaciones desde junio. Consulta y análisis de logs en Kubernetes, soporte de aplicaciones .NET y Vue, trabajo con pipelines CI/CD en Azure DevOps, Python y ServiceNow. En ausencia del focal point, apoyo en la coordinación del equipo y el seguimiento de tareas operativas."
            }
        ],
        "educacion": [
            {
                "titulo": "Administración de Sistemas Informáticos en Red (ASIR)",
                "institucion": "Formación Profesional de Grado Superior",
                "fecha": "Finalizado",
                "descripcion": "Formación en administración de sistemas operativos, redes y servicios, bases de datos y seguridad. Práctica de instalación, configuración y mantenimiento de infraestructuras informáticas."
            },
            {
                "titulo": "Curso de GitHub Actions: skills-hello-github-actions",
                "institucion": "GitHub Skills",
                "fecha": "Noviembre 2026",
                "descripcion": "Creación y ejecución de un workflow de GitHub Actions para automatizar tareas del repositorio y comprender cómo se ejecutan los flujos de trabajo.",
                "enlace": "https://github.com/Sergiomack91/skills-hello-github-actions/blob/main/README.md"
            }
        ],
        "skills": [
            "Kubernetes",
            "Azure DevOps",
            "Docker",
            "CI/CD",
            "Análisis de logs",
            "Python",
            ".NET",
            "Vue.js",
            "ServiceNow",
            "Prometheus",
            "Grafana",
            "Loki",
            "Troubleshooting"
        ],
        "intereses": [
            "Me encanta viajar",
            "Amante de los juegos de mesa y tiempo con amigos",
            "Tecnología: Confiabilidad de servicios, observabilidad y automatización.",
            "Deportes: Seguidor de la UD Almería, Snowboard, Crossfit, Padel.",
            "Música: Marea, Extremoduro, Natos y Waor, Reality."
        ],
        "proyectos": [
            {
                "nombre": "Infraestructura Cloud & Homelab",
                "descripcion": "Despliegue y administración de Kubernetes en un VPS con Traefik. Integra Prometheus y Grafana para métricas y dashboards, Loki para consulta de logs y alertas automatizadas por Telegram. Los workloads incluyen sondas de salud, solicitudes y límites de recursos y escalado horizontal.",
                "tecnologias": ["Kubernetes", "Traefik", "Grafana", "Loki", "IONOS VPS"]
            },
            {
                "nombre": "Pipeline CI/CD & GitOps",
                "descripcion": "Entrega automatizada del portfolio con GitHub Actions y despliegues declarativos en Kubernetes. Construcción y publicación de imágenes Docker, versionado por SHA y actualizaciones RollingUpdate para mantener el servicio durante los despliegues.",
                "enlace": "https://github.com/Sergiomack91/Proyecto-portfolio",
                "tecnologias": ["GitHub Actions", "Docker", "Python", "YAML"]
            },
            {
                "nombre": "Tienda online MIGS 3D",
                "descripcion": "Desarrollo de una página web para presentar la colección de productos impresos en 3D de mis amigos, con información sobre los materiales, las opciones de personalización y una vía de contacto para consultas.",
                "enlace": "https://migs3d.vercel.app/",
                "enlace_texto": "Ver página web",
                "tecnologias": ["Nuxt", "Vue.js", "JavaScript"]
            },
            {
                "nombre": "Sistema de Backups Automatizado",
                "descripcion": "Copias de seguridad automatizadas en Google Drive para proteger datos del servidor y manifiestos de infraestructura, facilitando su recuperación ante incidencias.",
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