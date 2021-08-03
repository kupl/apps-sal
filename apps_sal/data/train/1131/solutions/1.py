from collections import Counter
for _ in range(int(input())):
    a, b = map(int, input().split())
    ar = list(map(int, input().split()))
    ar = Counter(ar)
    dr = []
    for i in ar:
        if(ar[i] > b):
            dr.append(i)
    dr.sort()
    print(*dr)
