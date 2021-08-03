n = int(input())
x = []
l = 0
for i in range(n):
    m = int(input())
    for g in range(2, m + 1):
        for j in range(2, int(g**0.5) + 1):
            if g % j == 0:
                l = l + 1
        if l <= 0:
            x.append(g)
        l = 0
    print(sum(x))
    x.clear()
