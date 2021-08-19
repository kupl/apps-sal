l = []
for x in range(1, 100000):
    if x % 3 != 0:
        l.append(x ** 2)
for _ in range(int(input())):
    n = int(input())
    c = 0
    for x in l:
        if x <= n:
            c += 1
        else:
            break
    print(c)
