
mx1 = 0
mx2 = 0
sum = 0

def parsare(s, lista):
    number = ""
    for l in s:
        if l != " ":
            number += l
        else:
            lista.append(int(number))
            number = ""
    lista.append(int(number))

row1 = []
row2 = []
row3 = []

sir = input()
parsare(sir, row1)

sir = input()
parsare(sir, row2)

sir = input()
parsare(sir, row3)

for nr in row2:
    sum += nr * row1[1]
    if nr > mx1:
        mx2 = mx1
        mx1 = nr
    elif nr > mx2:
        mx2 = nr

ok = True
ok2 = False

for nr in row3:
    dif = nr - mx1
    if dif < 0:
        ok = False
        break
    elif dif == 0:
        ok2 = True
    sum += dif

if ok and ok2:
    print(sum)
elif ok:
    print(sum + mx1 - mx2)
else:
    print(-1)

