for _ in range(eval(input())):
    a, b, m = list(map(int, input().split()))
    gsum = (m + 1) * m / 2
    if gsum < min(a, b):
        print(a + b - 2 * gsum)
    else:
        print(abs(a - b))
