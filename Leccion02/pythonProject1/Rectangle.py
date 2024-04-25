"""
Instrucciones:
- Calcular el área y el perímetro de un rectángulo

Proporciona el alto:
Proporciona el ancho:
Area: <area>
Permietro: <perimetro>
"""
alto = int(input("Alto del rectangulo: "))
ancho = int(input("Ancho del rectangulo: "))

print(f'Area: {alto * ancho}')
print(f'Perimetro: {(alto + ancho) * 2}')