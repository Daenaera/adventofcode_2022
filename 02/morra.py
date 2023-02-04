gioco = open("input.txt" , "r");

lost = 0
draw = 3
won = 6

X = 1 
Y = 2 
Z = 3 

ris = 0

for linea in gioco:
    if linea[2] == "X":
        ris += X
        if linea[0] == "A":
            ris += draw
        elif linea[0] == "C":
            ris += won
        else: ris += lost

    if linea[2] == "Y":
        ris += Y
        if linea[0] == "B":
            ris += draw
        elif linea[0] == "A":
            ris += won
        else: ris += lost

    if linea[2] == "Z":
        ris += Z
        if linea[0] == "C":
            ris += draw
        elif linea[0] == "B":
            ris += won
        else: ris += lost

print(ris)