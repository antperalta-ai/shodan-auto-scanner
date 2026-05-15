import os
import shodan
import socket

def main():
    # REQUISITO: Variables de entorno (Prohibido hardcoding)
    api_key = os.environ.get('SHODAN_API_KEY')
    # Si el usuario no pasa una IP, usamos una de respaldo para evitar que falle el pipeline
    target_ip = os.environ.get('TARGET_IP', '8.8.8.8') 

    # ERROR TIPO 1: Validar si falta la clave de la API (Error de configuración)
    if not api_key:
        print("ERROR TIPO 1 (Configuración): La variable de entorno SHODAN_API_KEY no existe o está vacía.")
        exit(1)

    print(f"[*] Iniciando escaneo OSINT automatizado para la IP: {target_ip}...")
    
    try:
        # Configurar un timeout global para la conexión (para probar errores de timeout)
        socket.setdefaulttimeout(10) 
        
        # Conexión con la API
        api = shodan.Shodan(api_key)
        host = api.host(target_ip)
        
        # REQUISITO: Procesar al menos 3 campos de datos
        ip_str = host.get('ip_str', 'N/A')      # Campo 1
        org = host.get('org', 'N/A')            # Campo 2
        os_name = host.get('os', 'N/A')         # Campo 3
        ports = host.get('ports', [])           # Campo 4 (Extra)
        
        print("\n--- RESULTADOS DEL ESCANEO ---")
        print(f"1. Dirección IP    : {ip_str}")
        print(f"2. Organización    : {org}")
        print(f"3. Sistema Oper.   : {os_name}")
        print(f"4. Puertos Abiertos: {ports}")
        print("------------------------------\n")
        
    # ERROR TIPO 2: Manejo de errores de la API (Ej: 404 IP no encontrada, clave inválida)
    except shodan.APIError as e:
        print(f"ERROR TIPO 2 (API de Shodan): {e}")
        exit(1)
        
    # ERROR TIPO 3: Manejo de Timeout (Si el servidor tarda en responder)
    except TimeoutError:
        print("ERROR TIPO 3 (Timeout): La conexión con la API de Shodan excedió el tiempo límite.")
        exit(1)
        
    # ERROR TIPO 4: Errores a nivel de red (Fallo de DNS, desconexión)
    except socket.error as e:
        print(f"ERROR TIPO 4 (Red): Fallo de conexión o red detectado -> {e}")
        exit(1)
        
    # Catch-all de seguridad
    except Exception as e:
        print(f"ERROR INESPERADO: Ocurrió un problema no catalogado -> {e}")
        exit(1)

if __name__ == '__main__':
    main()
