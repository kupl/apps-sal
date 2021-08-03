import math


def niceness(a):
    nice = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            nice += math.gcd(a[i], a[j])
    return nice


def f(a, s):
    if -1 not in a:
        if s != 0:
            return ()
        return (tuple(a),)
    if s == 0:
        return ()
    idx = a.index(-1)
    ans = ()
    for i in range(1, s + 1):
        a[idx] = i
        ans += f(a, s - i)
        a[idx] = -1
    return ans


def __starting_point():
    t = int(input())
    numbers = [0] * 50
    mod = 10**9 + 7
    for i in range(1, 51):
        numbers[i - 1] = i
    for i in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        ans, ss = 0, 0
        for x in range(len(a)):
            if(a[x] != -1):
                ss += a[x]
        x = f(a, s - ss)
        for i in x:
            ans += niceness(i)
        print(ans % mod)


__starting_point()
