t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(n):
        l[i] = l[i] % 6
        if l[i] == 0:
            l[i] = 6
    ans = sum(l)
    print(ans)
