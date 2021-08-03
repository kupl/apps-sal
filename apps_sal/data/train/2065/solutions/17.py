n, k = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(k)]

for row in m:
    if row[1] == 1:
        for idx in range(1, row[0] + 1):
            if row[idx] != idx:
                idx -= 1
                break
        break
ans = (n - 1) + (n - k) - 2 * (idx - 1)
print(ans)
