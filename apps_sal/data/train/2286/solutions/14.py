import sys
sys.setrecursionlimit(10**6)
k, n = map(int, input().split())


def calc_x(K, N):
    return (pow(K, N + 1) - K) // (K - 1)


def lexico(K, N, X):
    #print(K, N, X)
    nonlocal ans
    if X == 0:
        return
    q = (calc_x(K, N - 1) + 1)
    if N > 1:
        ans.append((X // q) + 1)
    else:
        ans.append((X // q))
    lexico(K, N - 1, (X - 1) % q)


if k == 1:
    print(*[1 for _ in range((n + 1) // 2)])
elif n == 1:
    print((k + 1) // 2)
elif k % 2 == 0:
    ans = [k // 2] + [k] * (n - 1)
    print(*ans)
else:
    if n % 2 == 1:
        cur, i = 1, n
    else:
        cur, i = 0, n
    while cur <= i:
        i -= 1
        cur += pow(k, n - i)
    ans = [(k + 1) // 2] * i
    ind = (cur - i) // 2
    lexico(k, n - i, ind)
    print(*ans)
