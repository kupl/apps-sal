from collections import Counter
try:
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        d = dict(Counter(a))
        new = []
        for i in range(0, n):
            if i in d:
                new.append(i)
            else:
                new.append(0)
        print(*new)
except:
    pass
