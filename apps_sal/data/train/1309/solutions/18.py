
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = []
    for i in range(1, n + 1):
        a.append(i)
    a = a[::-1]
    for j in a:
        print(j, end="")
    print()
    for i in range(n - 1):
        a[i] = "*"
        for j in a:
            print(j, end="")
        print()
