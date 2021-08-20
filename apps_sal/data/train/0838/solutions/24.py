t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    w = list(map(int, input().strip().split(' ')))
    ans = 0
    for i in range(len(w)):
        ans = max(w[i] + i, ans)
    print(ans)
