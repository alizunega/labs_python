import random

temps = [[0.0 for h in range(24)] for d in range(31)]

for h in range(24):
    for d in range(31):
        temps[d][h] = round(random.uniform(1, 40), 2)
        
print(temps)        

total = 0.0

for day in temps:
    total += day[11]

average = round((total/31), 2)

print("La temperatura promedio del mes al mediodia es: ", average)
