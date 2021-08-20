import functools


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


for _ in range(int(input())):
    (n, m) = map(int, input().split())
    p = list(map(int, input().split()))
    ans = functools.reduce(lambda x, y: gcd(x, y), p)
    if ans <= n:
        print(n - ans)
    else:
        f = [1]
        for k in range(ans // 2, 1, -1):
            if ans % k == 0:
                if k <= n:
                    f.append(k)
                if ans // k <= n:
                    f.append(ans // k)
        res = n - max(f)
        print(res)
