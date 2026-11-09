import requests

# Tu URL pública real de Render
BASE_URL = "https://repositorioangel.onrender.com"

print("=== INICIANDO PRUEBAS DE LA API EN RENDER ===")

# Prueba 1: Endpoint raíz (GET /)
try:
    response = requests.get(f"{BASE_URL}/")
    print("\n[Prueba 1] GET /")
    print("Estado HTTP:", response.status_code)
    print("Respuesta:", response.json())
except Exception as e:
    print("Error en Prueba 1:", e)

# Prueba 2: Endpoint de saludo (GET /saludo/usuario)
try:
    response = requests.get(f"{BASE_URL}/saludo/Angel")
    print("\n[Prueba 2] GET /saludo/Angel")
    print("Estado HTTP:", response.status_code)
    print("Respuesta:", response.json())
except Exception as e:
    print("Error en Prueba 2:", e)

print("\n=== PRUEBAS FINALIZADAS ===")