# Ejemplo mínimo
linea = "2026-10-12 08:23:30|ERROR|payment_gateway|Timeout en la respuesta"
campos = linea.split("|")
print(campos)

print(campos[1]) # Resultado: "ERROR"
print(len(campos)) # Resultado: 4