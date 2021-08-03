try:
    for i in range(int(input())):
        n = int(input())
        s = input()
        l = list(map(int, s))
        d = int(input())
        p = list(map(int, input().split()))
        for j in range(d):
            l.insert(p[j] - 1 + l.count('|'), '|')
            a = 0
            n = len(l)
            while a < n:
                if l[a] == 1:
                    if a > 0:
                        if l[a - 1] == 0:
                            l[a - 1] = 1
                    if a < n - 1:
                        if l[a + 1] == 0:
                            l[a + 1] = 1
                            a += 1
                a += 1
        print(l.count(1))
except:
    pass
