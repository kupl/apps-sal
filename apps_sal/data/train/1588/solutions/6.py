from operator import itemgetter
t = int(input())
for _ in range(t):
    n = int(input())
    di = {}
    for i in range(n):
        (a, b) = input().split()
        b = int(b)
        di.setdefault(b, [])
        di[b].append(a)
    f = 0
    for item in sorted(di):
        if len(di[item]) == 1:
            print(di[item][0])
            f = 1
            break
    if f == 0:
        print('Nobody wins.')
