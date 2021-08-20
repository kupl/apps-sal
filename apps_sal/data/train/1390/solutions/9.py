for _ in range(int(input())):
    (a, b) = map(int, input().split())
    print(b * (a + b + 1) / (b + 1))
