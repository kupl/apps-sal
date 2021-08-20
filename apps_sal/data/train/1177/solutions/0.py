def nCr(n, k):
    if k > n:
        return 0
    k = min(k, n - k)
    (num, den) = (1, 1)
    for i in range(k):
        num *= n - i
        den *= i + 1
    return num / den


def Main():
    for cases in range(int(input())):
        (a, b) = [int(x) for x in input().split()]
        print(nCr(a, b))


Main()
