t = int(input())
for _ in range(t):
    (v, w) = map(int, input().split())
    ans = min(v, w)
    print(ans + 1)
