v = int(input())
eps = 170

def ans(a):
    a.sort()
    if len(a) % 2 == 0:
        med = a[len(a)//2]
    else:
        med = (a[len(a)//2] + a[len(a)//2 - 1]) // 2

    l = med - med // 2
    r = med + med // 2

    c1 = c2 = 0

    for i in a:
        if i >= l and i <= r:
            c1 += 1
        else:
            c2 += 1

    if abs(c1 - c2) <= eps:
        return (med, "uniform")
    else:
        return (med, "poisson")

    

for i in range(v):
    cur = [int(i) for i in input().split()]
    b = ans(cur)
    if b[1] == "poisson":
        print(b[0])
    else:
        print((max(cur) - min(cur)) // 2)
        
        

