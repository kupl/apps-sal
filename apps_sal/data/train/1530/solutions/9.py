
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = []
    s = n * (n + 1) // 2
    for i in range(1, n + 1):
        s = i * (i + 1) // 2
        for j in range(i):

            print(s, end="")
            s -= 1
        print()
