def gets():
    while(1):
        a = input().strip()
        if(a):
            return a


def solve(n, k):
    if(k > n):
        return 0
    k = min(k, n - k)
    num, den = 1, 1
    for i in range(k):
        num *= (n - i)
        den *= (i + 1)
    return num / den


def Main():
    for cases in range(int(gets())):
        a, b = [int(x) for x in gets().split()]
        print(solve(a, b))


Main()
