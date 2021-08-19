t = int(input())
for t in range(t):
    n = int(input())
    k = 2
    for i in range(1, n + 1):
        s = k
        for j in range(1, n + 1):
            print(s, end='')
            s += 1
        k += 1
        print()
