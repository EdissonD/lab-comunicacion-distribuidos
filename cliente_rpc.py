import xmlrpc.client

# Crear proxy
proxy = xmlrpc.client.ServerProxy(
    "http://localhost:8080/"
)

print("===== PRUEBAS RPC IMC =====\n")

# Caso correcto 1
resultado1 = proxy.calcular_imc(70, 1.75)
print("Caso 1:")
print(resultado1)
print()

# Caso correcto 2
resultado2 = proxy.calcular_imc(95, 1.70)
print("Caso 2:")
print(resultado2)
print()

# Caso de error
resultado3 = proxy.calcular_imc(-10, 1.80)
print("Caso 3 (error):")
print(resultado3)
print()

# Caso de error
resultado4 = proxy.calcular_imc(80, 0)
print("Caso 4 (error):")
print(resultado4)
print()

# Otro caso correcto
resultado5 = proxy.calcular_imc(50, 1.60)
print("Caso 5:")
print(resultado5)
print()

# Mostrar historial
print("===== HISTORIAL =====")
historial = proxy.historial()

for item in historial:
    print(item)