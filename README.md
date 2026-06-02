# Portfolio Técnico - Arquitectura Cloud Native & DevOps

Este repositorio contiene el código fuente y la Infraestructura como Código (IaC) para el despliegue automatizado de mi portfolio personal. El proyecto está diseñado y operado bajo principios de **Alta Disponibilidad (HA)**, **Self-Healing** y **GitOps**, simulando un entorno de producción corporativo.

🌐 **Entorno de Producción:** [https://www.pruebasergio.com](https://www.pruebasergio.com)

---

## 🏗️ Arquitectura del Sistema

El sistema está orquestado sobre un clúster de Kubernetes (K3s) y se divide en los siguientes componentes principales:

* **Frontend:** SPA desarrollada en Vue.js, servida de forma ligera.
* **Backend:** API REST desarrollada en Python.
* **Ingress Controller:** Traefik v2 gestionando el enrutamiento y los Middlewares (redirecciones de HTTP a HTTPS y de bare-domain a www).
* **Gestión de Certificados:** Cert-Manager integrado con Let's Encrypt para la renovación automática de certificados SSL/TLS.
* **Observabilidad:** Stack completo de `kube-prometheus-stack` (Prometheus, Alertmanager y Grafana) para la monitorización en tiempo real de nodos y pods.

---

## 🛡️ Resiliencia y Control de Recursos (Ingeniería de Fiabilidad)

Para garantizar la estabilidad del nodo y la experiencia del usuario bajo estrés, los despliegues de Kubernetes implementan las siguientes políticas:

1. **Gestión de Recursos (QoS):** Todos los contenedores tienen configurados `Requests` y `Limits` estrictos de CPU y Memoria RAM para evitar la saturación del servidor (OOMKilled) y el efecto "vecino ruidoso".
2. **Horizontal Pod Autoscaling (HPA):** Escalado dinámico basado en métricas. El frontend y el backend escalan automáticamente sus réplicas si el consumo de CPU supera el umbral objetivo del 70-75%, repartiendo la carga ante picos de tráfico repentinos.
3. **Sondas de Salud (Probes):** Implementación de `Liveness` y `Readiness` probes mediante comprobaciones TCP. El clúster aísla automáticamente los contenedores que no están listos para recibir tráfico y reinicia automáticamente aquellos que sufren bloqueos internos (*Self-Healing*).
4. **Zero-Downtime Deployments:** Estrategia de `RollingUpdate` garantizada durante las subidas a producción.

---

## ⚙️ Integración y Despliegue Continuo (CI/CD)

El ciclo de vida del software está completamente automatizado a través de **GitHub Actions**. Al integrar código en la rama `main`, el pipeline ejecuta de forma desatendida:

1. Construcción de imágenes Docker para Frontend y Backend.
2. Push de las imágenes etiquetadas al registro de Docker Hub.
3. Sincronización segura por SSH de los manifiestos declarativos (`.yaml`) ubicados en la carpeta `/k8s` hacia el servidor VPS.
4. Aplicación de los cambios de infraestructura (`kubectl apply`) y reinicio de los *Deployments* para inyectar las nuevas versiones sin cortes de servicio.

---

## 📂 Estructura de Directorios Principal

* `/frontend/`: Código fuente de la aplicación Vue.js y su respectivo `Dockerfile`.
* `/backend/`: Código fuente de la API en Python y su respectivo `Dockerfile`.
* `/k8s/`: Manifiestos declarativos de Kubernetes (Deployments, Services, Ingress, HPA, Middlewares, etc.).
* `/.github/workflows/`: Definición de los pipelines de CI/CD.

---

👨‍💻 Autor
Sergio Rodríguez Quintana
Especialista en Sistemas Cloud, DevOps y Administración de Redes.