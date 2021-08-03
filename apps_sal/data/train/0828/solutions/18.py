t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if len(set(l)) == 1 and l[0] == 1:
        print(0)
    elif len(set(l)) == 1 and l[0] == 0:
        print(n * 1100)
    else:
        f = 1
        c = 0
        for j in range(n):
            if l[j] == 1 and f == 0:
                c = c + 100
            elif l[j] == 0:
                c = c + 1100
                f = 0
        print(c)
