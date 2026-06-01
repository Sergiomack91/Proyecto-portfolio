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

⚙️ Flujo de CI/CD (GitHub Actions)
El despliegue está totalmente automatizado. Cada vez que se realiza un push a la rama main, el pipeline de GitHub Actions ejecuta las siguientes fases:

Checkout: Clona el código más reciente del repositorio.

Build & Push: Construye las imágenes Docker actualizadas tanto para el frontend como para el backend y las sube a Docker Hub.

Deploy: Se conecta de forma segura al clúster K3s a través de SSH y aplica los manifiestos de Kubernetes para reiniciar los pods con las nuevas imágenes de forma transparente (Zero-Downtime Deployment).

🔒 Gestión de Red y Seguridad (Ingress & Middlewares)
El clúster está configurado para gestionar el tráfico de forma inteligente mediante Traefik:

Subdominios dinámicos: La API responde en api.pruebasergio.com, mientras que el frontend responde en www.pruebasergio.com.

Redirecciones automáticas: Se han implementado Traefik Middlewares nativos (redirectRegex y redirectScheme) para asegurar que todo el tráfico entrante desde http:// o sin las www sea enrutado a una conexión 100% segura.

Auto-SSL: cert-manager negocia y renueva los certificados criptográficos en la sombra sin intervención manual.

👨‍💻 Autor
Sergio Rodríguez Quintana
Especialista en Sistemas Cloud, DevOps y Administración de Redes.