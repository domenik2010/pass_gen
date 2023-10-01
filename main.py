import random
simvols="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
size=int(input("укажите длину пароля: "))
pswd='' 
for i in range(size):
    pswd += random.choice(simvols)
print(pswd)