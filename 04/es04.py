import re

coppie = open("input04.txt", "r")

conto = 0
sovrapp = 0

for linea in coppie:
    y = re.split(r'\D+', linea)
    numero1 = int(y[0])
    numero2 = int(y[1])
    numero3 = int(y[2])
    numero4 = int(y[3])

    #prima parte
    if numero1 >= numero3 and numero2 <= numero4:
        conto += 1
    elif numero1 <= numero3 and numero2 >= numero4:
        conto +=1


    #seconda parte
    list1 = list(range(numero1, numero2+1))
    list2 = list(range(numero3, numero4+1))
    
    
    def parte2(list1, list2):
        for n in list1:
            if n in list2:
                return True
    
    if parte2(list1, list2) == True:
        sovrapp +=1


print(conto)
print(sovrapp)