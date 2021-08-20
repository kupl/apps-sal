t = int(input())
for test in range(t):
    (n, p) = map(int, input().split())
    m = round(n / 2 - 0.7)
    if m == 0:
        choices = p ** 3
    else:
        choices = (p - m) ** 2 + (p - n) ** 2 + (p - m) * (p - n)
    print(choices)
