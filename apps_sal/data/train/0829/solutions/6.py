n = int(input())
z = []
s = list(map(int, input().split()))[:n]
for i in range(0, n):
    for j in range(i + 1, n):
        p = abs(s[i] - s[j])
        z.append(p)
print(sum(z))
