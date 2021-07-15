n = int(input())
mas = []
maxx = 0
for i in range(n):
    mas.append(input())
for i in range(7):
    ses = 0
    for ii in range(n):
        if mas[ii][i] == '1':
            ses += 1
    if ses > maxx:
        maxx = ses
print(maxx)

