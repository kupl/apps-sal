t = int(input())
for t in range(t):
    n = int(input())
    s = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(s, end='')
            s += 1
        print()
