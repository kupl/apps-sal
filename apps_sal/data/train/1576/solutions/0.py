for a0 in range(int(input())):
    n = int(input())
    l = []
    for i in range(1, n + 1):
        l.append(i)
    for j in range(n):
        s = ''
        for k in l:
            s += str(k)
        print(s)
        x = l[0]
        l.pop(0)
        l.append(x)
