# cook your dish here
t = int(input())
for i in range(t):
    a = int(input())
    i = 1
    l = []
    p = 0
    dene = 0
    lene = 0
    while(p >= 0):
        dene = dene + pow(2, i - 1)
        lene = lene + a
        p = lene - dene
        i = i + 1
        l.append(p)
    print(i - 2, l.index(max(l)) + 1)
