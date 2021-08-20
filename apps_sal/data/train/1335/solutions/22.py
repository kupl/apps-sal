from itertools import groupby
try:
    N = int(input())
    sweet = list(map(int, input().split()))
    sweet = sorted(sweet)
    l = [len(list(group)) for (key, group) in groupby(sweet)]
    for i in range(len(l)):
        if l[i] % 2 == 0:
            pass
        else:
            l[i] += 1
    print(sum(l) // 2)
except:
    pass
