# Solicitar los valores RGB al usuario y validar la entrada
while True:
     try:
         r = int(input("Introduce el valor RGB para el color rojo (0-255): "))
         if r < 0 or r > 255:
            raise ValueError
         break
     except ValueError:
         print("El valor debe ser un entero entre 0 y 255")
 
while True:
      try:
         g = int(input("Introduce el valor RGB para el color verde (0-255): "))
         if g < 0 or g > 255:
             raise ValueError
         break
      except ValueError:
         print("El valor debe ser un entero entre 0 y 255")
 
while True:
     try:
         b = int(input("Introduce el valor RGB para el color azul (0-255): "))
         if b < 0 or b > 255:
             raise ValueError
         break
     except ValueError:
         print("El valor debe ser un entero entre 0 y 255")
 
 # Convertir los valores RGB a su valor hexadecimal correspondiente
valor_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
 
 # Mostrar el valor hexadecimal
print("h= ({}, {}, {}) es {}".format(r, g, b, valor_hex))
