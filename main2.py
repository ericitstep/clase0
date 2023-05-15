# Solicitar entradas del usuario
n1 = int(input("Ingrese el numerador de la primer fracción: "))
d1 = int(input("Ingrese el denominador de la primer fracción: "))
n2 = int(input("Ingrese el numerador de la segunda fracción: "))
d2 = int(input("Ingrese el denominador de la segunda fracción: "))

# Encontrar el minimo comun multiplo para denominadores
mcm = d1
while mcm % d2 != 0:
    mcm += d1

# Convertir fracciones al mismo denominador
n1 = n1 * (mcm // d1)
d1 = mcm
n2 = n2 * (mcm // d2)
d2 = mcm

# Sumar fracciones
suma = n1 + n2

# Encontrar el minimo comun multiplo para simplificar la fracción resultante
mcd = 1
for i in range(1, min(suma, mcm) + 1):
    if suma % i == 0 and mcm % i == 0:
        mcd = i

# Simplificar la fracción resultante
numerador = suma // mcd
denominador = mcm // mcd

# Imprimir resultado
print("r=", numerador, "/", denominador)
