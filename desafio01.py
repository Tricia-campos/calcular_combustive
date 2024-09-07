hr1 = int(input("Digite a primeira hora: "))
min1 = int(input("digite o primeiro minuto: "))
hr2 = int(input("Digite a segunda hora: "))
min2 = int(input("digite o segundo minuto: "))

if hr1 > 12:
    hr1 -= 12
if hr2 > 12:
    hr2 -= 12

horas = hr1 + hr2
minutos = min1 + min2

if minutos >= 60:
    horas = horas + 1
    minutos = minutos - 60

if horas >= 12:
    horas -= 12
print(f"{horas} : {minutos}")
