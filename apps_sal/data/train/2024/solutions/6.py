n = int(input())
p = list(map(float, input().split()))
p.append(0)
s = [p[0]] * 3
s[2] = 0
ans = (2 * s[2] + s[1]) * (1 - p[1])
for i in range(1, n):
    s[0] += 1 - p[i - 1]
    for j in range(2, 0, -1):
        s[j] += s[j - 1]
    for j in range(3):
        s[j] *= p[i]
    ans += (2 * s[2] + s[1]) * (1 - p[i + 1])
print(ans)
