n = int(input())
nm = [0] + list(map(int, input().split())) + [-1]
sm = [0] * len(nm)
for i in range(n + 1, 0, -1):
    if not nm[i]:
        sm[i - 1] = sm[i] + 1
    else:
        sm[i - 1] = sm[i]
ans = 0
for i in range(1, n + 1):
    if nm[i]:
        ans += sm[i]
print(str(ans))
