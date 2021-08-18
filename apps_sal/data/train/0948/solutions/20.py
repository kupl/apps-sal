a, b = map(int, input().split())
ans = 0
for x in range(1, a + 1):
    m = 1
    y = 0
    while y < b:
        y = m * (2 * x + m)
        if y > b:
            break
        ans += 1
        m += 1
print(ans)
