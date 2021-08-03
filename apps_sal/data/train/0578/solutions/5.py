def function(x, n):
    if x > n:
        return 0
    return x * (n - x * b)


for _ in range(int(input())):
    n, b = list(map(int, input().split()))
    # print(n//(2*b),n//(2*b)+1)
    print(max((function(n // (2 * b), n), function(n // (2 * b) + 1, n))))
