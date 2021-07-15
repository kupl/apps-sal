t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    id = list(zip(l,list(range(n))))
    id.sort()
    val, pos = zip(*id)
    best = 1
    i = 1
    count = 1
    while True:
        if i >= n:
            break
        if pos[i] > pos[i-1]:
            count += 1
            best = max(count,best)
        else:
            count = 1
        i += 1
    print(n-best)
