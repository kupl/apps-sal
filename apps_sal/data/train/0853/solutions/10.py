t = int(input())
name = list()
time = list()
ro = list()
for i in range(t):
    n = int(input())
    for j in range(n):
        name.append(input())
        time.append(int(input()))
    p = time.copy()
    time.sort()
    for x in range(len(time)):
        for y in range(len(p)):
            if time[x] == p[y]:
                ro.append(y)
    for m in ro:
        print(name[m])
    name.clear()
    time.clear()
    ro.clear()
    p.clear()
