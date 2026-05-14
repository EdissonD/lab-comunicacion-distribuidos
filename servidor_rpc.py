from xmlrpc.server import SimpleXMLRPCServer

# Lista para guardar historial
historial_calculos = []


def calcular_imc(peso_kg, altura_m):
    """
    Calcula el IMC y retorna categoría.
    Maneja errores de entrada.
    """

    global historial_calculos

    # Validaciones
    if peso_kg <= 0 or altura_m <= 0:
        return {
            "error": "Peso y altura deben ser mayores que cero."
        }

    # Fórmula IMC
    imc = peso_kg / (altura_m ** 2)

    # Determinar categoría
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"

    resultado = {
        "peso": peso_kg,
        "altura": altura_m,
        "imc": round(imc, 2),
        "categoria": categoria
    }

    # Guardar historial
    historial_calculos.append(resultado)

    # Mantener solo últimos 5
    historial_calculos = historial_calculos[-5:]

    return resultado


def historial():
    """
    Retorna últimos 5 cálculos.
    """
    return historial_calculos


# Crear servidor RPC
server = SimpleXMLRPCServer(
    ("localhost", 8080),
    allow_none=True,
    logRequests=True
)

print("Servidor RPC escuchando en puerto 8080...")

# Registrar funciones
server.register_function(calcular_imc, "calcular_imc")
server.register_function(historial, "historial")

# Ejecutar servidor
server.serve_forever()