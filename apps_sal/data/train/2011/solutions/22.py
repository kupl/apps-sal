n = int(input())
ans = 0
l = []
for m in range(max(n - 82, 1), n):
    if m + sum(map(int, [d for d in str(m)])) == n:
        ans += 1
        l.append(m)
print(ans)
for d in l:
    print(d)
