t = int(input())
for i in range(t):
    k = int(input())
    n = list(map(int, input().split()))
    s = 0
    for j in n:
        if j % 2 == 0:
            s += j
    print(s)
