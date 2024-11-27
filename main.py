import random

caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud=int(input("Ingresa la longitud de tu contraseña: "))
contrasena=""
for i in range(longitud):
    contrasena += random.choice(caracteres)

print(f"Tu contraseña es: {contrasena}")
