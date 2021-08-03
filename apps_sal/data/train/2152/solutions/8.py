def f(n):
    minus = n // 2 if n % 2 == 0 else 0
    n //= 2
    return n * (n + 1) - minus


def cal(a, k):
    ans = 0
    cur = 0

    for i, x in enumerate(a):
        if x == 0:
            ans += min(cur, k - cur)
        else:
            cur += 1
    return ans + f(k)


def uoc(x):
    i = 1
    arr = []
    while i * i <= x:
        if x % i == 0:
            arr.append(i)

            if i * i != x:
                arr.append(x // i)
        i += 1
    return sorted(arr)[1:]


n = int(input())
a = list(map(int, input().split()))
min_ = float('inf')

for u in uoc(sum(a)):
    cur = 0
    l = None
    s = 0

    for i, x in enumerate(a):
        if x == 1:
            cur += 1
            if l == None:
                l = i
            if cur == u:
                s += cal(a[l:i + 1], u)
                cur, l = 0, None
    min_ = min(min_, s)

if min_ < float('inf'):
    print(min_)
else:
    print(-1)
