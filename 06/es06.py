
segnale = open("input06.txt", "r")

indicatore = []
messaggio = []
pos = 0

def lettere(pos, y, x):
      if len(y) == x:
            if len(y) != len(set(y)):
                  y.pop(0)
            else:
                  print(pos)

for linea in segnale:
      for c in linea:
            pos += 1
            messaggio += c
            lettere(pos, messaggio, 14)
            indicatore += c
            lettere(pos, indicatore, 4)






