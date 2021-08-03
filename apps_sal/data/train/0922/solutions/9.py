from collections import Counter
for _ in range(int(input())):
    n, m = map(int, input().split())
    ar = list(map(int, input().split()))
    br = list(map(int, input().split()))
    cr = ar + br
    cr = Counter(cr)
    dr = []
    for i in cr:
        if(cr[i] == 1):
            dr.append(i)
    dr.sort()
    print(*dr)
