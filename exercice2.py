for i in range(2,21,2):
    print(i)
print("les 10 premiers nombre paires")

count = 1
number = 1
while count <= 10: 
    print(number)
    number +=2
    count +=1
print("les 10 premiers nombre impaires")

def demander_nombre():
     while True:
        nombre = int(input("veuillez entrer un nombre : "))
        return nombre 
print("")