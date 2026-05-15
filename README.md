# Shodan Recon Auto-Scanner 🔍

Asignatura: Programación y Redes Virtualizadas (DRY7122)
Antuan Peralta 

## Contexto y Narrativa del Proyecto

**Stakeholders:**
Esta herramienta está diseñada para Administradores de Redes, Analistas de Ciberseguridad y Estudiantes del área de redes y seguridad informática.

**Propuesta de Valor (Problema / Solución):**
* **El Problema:** Los profesionales y estudiantes de seguridad necesitan identificar rápidamente qué servicios, puertos y posibles vulnerabilidades se encuentran expuestos en una dirección IP pública. Realizar escaneos activos (como Nmap) consume tiempo, requiere configuraciones complejas y puede levantar alertas en los firewalls o sistemas IDS/IPS del objetivo.
* **La Solución:** Esta aplicación resuelve la dificultad proporcionando una consulta automatizada, rápida y 100% pasiva (OSINT) utilizando la API de Shodan. Permite al usuario obtener un resumen claro en consola de la información crítica de la IP (Organización, Sistema Operativo, Puertos y Vulnerabilidades) de forma segura y estandarizada a través de contenedores Docker, facilitando la toma de decisiones o el aprendizaje sin tocar la infraestructura real del objetivo.

export SHODAN_API_KEY="tu_clave_real"
export TARGET_IP="8.8.8.8"

Método 1: Desde tu Terminal Local (Máquina devasc)
Simplemente sobrescribes la variable en la memoria y vuelves a ejecutar tu automatización.

Abre tu terminal.

Exporta la nueva IP (por ejemplo, la de Cloudflare):

Bash
export TARGET_IP="1.1.1.1"


Ejecuta el script:

Bash
./build.sh
¡Y listo! Verás los datos de Cloudflare en tu pantalla.

Método 2: Desde Jenkins (Para demostrar tu automatización)
Actualmente, le dijimos a Jenkins que escaneara 8.8.8.8 en el paso de construcción. Para cambiarlo:

Ve a tu Jenkins y entra al trabajo BuildAppJob.

Haz clic en "Configure" (Configurar) en el menú izquierdo.

Baja del todo hasta la sección Build Steps (donde pusiste el código de Execute shell).

Cambia la línea export TARGET_IP="8.8.8.8" por la IP que quieras. Por ejemplo:
export TARGET_IP="208.67.222.222" (Ese es el DNS de Cisco OpenDNS).

Guarda los cambios.

Ve a tu SamplePipeline y haz clic en "Build Now".

Automáticamente, Jenkins hará todo el trabajo por ti usando la nueva IP.

¡Felicidades por completar este proyecto! Has integrado desarrollo en Python, ciberseguridad, infraestructura con Docker y CI/CD con Jenkins. Es un excelente trabajo a nivel técnico.
