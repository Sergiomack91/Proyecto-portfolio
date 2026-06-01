# 🚀 Portfolio Web App - Cloud & DevOps Infrastructure

Este repositorio contiene el código fuente y la configuración de infraestructura de mi portfolio personal. El proyecto destaca por una arquitectura moderna, contenerizada y orquestada, desplegada bajo prácticas de Integración y Despliegue Continuo (CI/CD).

🌍 **Live Demo:** [https://www.pruebasergio.com](https://www.pruebasergio.com)

---

## 🛠️ Stack Tecnológico y Arquitectura

El proyecto está dividido en microservicios y gestionado íntegramente mediante orquestación de contenedores.

**Desarrollo:**
* **Frontend:** Vue.js 3 (Production Build) + HTML/CSS
* **Backend / API:** Python + FastAPI
* **Contenedores:** Docker

**Operaciones e Infraestructura (Cloud):**
* **Orquestación:** Kubernetes (K3s) desplegado en un VPS (Ubuntu).
* **Enrutamiento y Proxy Inverso:** Traefik Ingress Controller.
* **Seguridad y SSL:** Certificados automáticos Let's Encrypt gestionados mediante `cert-manager`.
* **Middlewares:** Redirección forzada de HTTP a HTTPS y de dominio raíz a subdominio `www` a nivel de clúster.
* **Seguridad del Servidor:** Acceso mediante llaves SSH y protección activa con Fail2Ban.

**Automatización:**
* **CI/CD Pipeline:** GitHub Actions (optimizadas para Node 24).
* **Registry:** Docker Hub.

---

## 🏗️ Estructura del Proyecto

El repositorio está organizado en las siguientes capas lógicas:

```text
.
├── .github/workflows/   # Pipelines de CI/CD para automatización de despliegues
├── backend/             # Código fuente y Dockerfile de la API en Python (FastAPI)
├── frontend/            # Código fuente, assets (SVG Favicons) y Dockerfile (Vue.js)
├── portfolio-k8s/       # Manifiestos de Kubernetes (Deployment, Service, Ingress, Middlewares)
└── README.md            # Documentación del proyecto