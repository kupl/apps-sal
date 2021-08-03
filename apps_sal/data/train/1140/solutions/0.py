for _ in range(int(input())):
    p, idx = map(int, input().split())
    b = bin(idx)[2:]
    b = ('0' * (p - len(b)) + b)[::-1]
    print(int(b, 2))
