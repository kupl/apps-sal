n = int(input())
for i in range(n):
    x = int(input())
    q = list(map(int, input().split()))
    r = []
    for i in q:
        if i not in r:
            r.append(i)
    print(*r)
