t = int(input())
for i in range(t):
    n = int(input())
    loss = 0
    for j in range(n):
        (p, q, d) = map(int, input().split())
        loss = loss + q * (p - (p - p * (d / 100)) * ((100 + d) / 100))
    print(loss)
