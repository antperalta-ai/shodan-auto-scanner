# Shodan Recon Auto-Scanner 🔍

## Contexto y Narrativa del Proyecto

**Stakeholders:**
Esta herramienta está diseñada para Administradores de Redes, Analistas de Ciberseguridad y Estudiantes del área de redes y seguridad informática.

**Propuesta de Valor (Problema / Solución):**
* **El Problema:** Los profesionales y estudiantes de seguridad necesitan identificar rápidamente qué servicios, puertos y posibles vulnerabilidades se encuentran expuestos en una dirección IP pública. Realizar escaneos activos (como Nmap) consume tiempo, requiere configuraciones complejas y puede levantar alertas en los firewalls o sistemas IDS/IPS del objetivo.
* **La Solución:** Esta aplicación resuelve la dificultad proporcionando una consulta automatizada, rápida y 100% pasiva (OSINT) utilizando la API de Shodan. Permite al usuario obtener un resumen claro en consola de la información crítica de la IP (Organización, Sistema Operativo, Puertos y Vulnerabilidades) de forma segura y estandarizada a través de contenedores Docker, facilitando la toma de decisiones o el aprendizaje sin tocar la infraestructura real del objetivo.


