n = int(input())
a = list(map(int, input().split()))
b = list(range(n))
s = list(map(list, zip(a, b)))
s.sort(reverse=True)
s.append([0, 0])
ans = [0] * n
for i in range(n):
    dif = s[i][0] - s[i + 1][0]
    ans[s[i][1]] += dif * (i + 1)
    if s[i + 1][1] > s[i][1]:
        s[i + 1][1] = s[i][1]
print(*ans, sep="\n")
