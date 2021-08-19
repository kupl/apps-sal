for a0 in range(int(input())):
    n = int(input())
    l = []
    for j in range(1, (n ** 2 + n) // 2 + 1):
        l.append(str(j))
    for i in range(n):
        s = ''
        x = l[:i + 1]
        x = x[::-1]
        for p in x:
            s += p
        print(s)
        l = l[i + 1:]
