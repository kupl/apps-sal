q = int(input())
s = [0] * 10
for i in range(10):
    for j in range(10):
        s[i] += (j * i) % 10

for i in range(q):
    n, m = list(map(int, input().split()))
    pages = n // m
    ans = s[m % 10] * (pages // 10)
    pages %= 10
    m %= 10
    for i in range(pages + 1):
        ans += (m * i) % 10
    print(ans)

