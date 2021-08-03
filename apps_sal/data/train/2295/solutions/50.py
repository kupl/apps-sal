n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
count = 0
m = 10**10
for a, b in ab:
    if a > b:
        m = min(m, b)
    count += a
if m == 10**10:
    print(0)
else:
    print(count - m)
