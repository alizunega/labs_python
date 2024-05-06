import random

# Función para simular el lanzamiento de una moneda
def lanzar_moneda():
    return random.choice(['cara', 'cruz'])

# Contadores para cara y cruz
contador_cara = 0
contador_cruz = 0

# Simular el lanzamiento de la moneda 100 veces
for _ in range(10):
    resultado = lanzar_moneda()
    if resultado == 'cara':
        contador_cara += 1
    else:
        contador_cruz += 1

    print(resultado)    

# Imprimir resultados
print("Número de veces que salió cara:", contador_cara)
print("Número de veces que salió cruz:", contador_cruz)
