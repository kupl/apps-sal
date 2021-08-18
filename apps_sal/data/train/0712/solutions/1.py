t = int(input())
for i in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    p = 0
    for j in q:
        if j % 2 != 0:
            p += 1
    if p == len(q):
        print("YES")
    else:
        print("NO")
