#a, b, h, w, n = map(int,input().split())
#rash = map(int,input().split())
n, c, d = list(map(int, input().split()))

fon = []

for i in range(n):
    s = input().split()
    kras = int(s[0])
    ctoim = int(s[1])
    if(s[2] == "C"):
        fon.append([kras, ctoim, True])
    else:
        fon.append([kras, ctoim, False])


def sravni(elem):
    return elem[0]


fon.sort(key=sravni, reverse=True)
# print(fon)

maxkras = 0
for fon1 in range(n):
    tekc = c
    tekd = d
    if fon[fon1][2]:
        tekc -= fon[fon1][1]
    else:
        tekd -= fon[fon1][1]
    if tekc < 0 or tekd < 0:
        continue
    fon2 = -1
    for i in range(fon1 + 1, n):
        if fon[i][2]:
            if fon[i][1] <= tekc:
                fon2 = i
                break
        else:
            if fon[i][1] <= tekd:
                fon2 = i
                break
    if not fon2 == -1:
        if fon[fon1][0] + fon[fon2][0] > maxkras:
            maxkras = fon[fon1][0] + fon[fon2][0]
print(maxkras)
