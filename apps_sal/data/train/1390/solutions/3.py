t = int(input())
while t > 0:
    (n, q) = list(map(int, input().split(' ')))
    print(q * n / (q + 1) + q)
    t -= 1
