try:
    t = int(input())
    for i in range(t):
        n = int(input())
        a = []
        avg = 0
        for j in range(n):
            t = list(input().split())
            avg = avg + float(t[2])
            a.append(t)
        avg /= n
        a.sort(key=lambda a: a[2])
        for x in a:
            if round(float(x[2])) <= round(avg):
                print(' '.join(map(str, x)))
except EOFError:
    pass
