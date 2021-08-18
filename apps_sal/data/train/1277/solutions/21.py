for _ in range(int(input())):
    n = int(input())
    loss = 0
    for t in range(n):
        p, q, d = map(int, input().split())
        ip = p + (p * (d / 100))
        fp = ip - (ip * (d / 100))
        loss += (p - fp) * q
    print(loss)
