
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = []
    for i in range(1, n + 1):
        a.append(i)
    for i in range(n):

        for i in a:
            print(i, end="")
        x = a[0]
        a.append(x)
        a.pop(0)
        print()
