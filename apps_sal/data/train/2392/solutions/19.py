t = int(input())
while (t > 0):
    t -= 1
    n, m = [int(x) for x in input().split()]
    tens = [(m * (i + 1)) % 10 for i in range(10)]
    tensum = sum(tens)
    c = n // m
    print(c // 10 * tensum + sum(tens[: c - (c // 10) * 10]))
