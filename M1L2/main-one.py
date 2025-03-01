import random

caract = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
    longitud = int(input("Indique la longitud de la contraseña (0 para salir): "))
    
    if longitud == 0:
        print("Saliendo del generador...")
        break 
    
    
    password = ""
    i = 0
    while i < longitud:
        password += random.choice(caract)
        i += 1

    print(password)  