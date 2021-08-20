def fib(n):
    F = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]


def multiply(F, M):
    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    if n == 0 or n == 1:
        return
    M = [[1, 1], [1, 0]]
    power(F, n // 2)
    multiply(F, F)
    if n % 2 != 0:
        multiply(F, M)


s = input()
nr = len(s)
M = 1000000007
cnt = 1
i = 0
while i < nr:
    if s[i] == 'c' or s[i] == 'k':
        cnt = 0
        break
    elif s[i] == 'g':
        val = 1
        i += 1
        while i < nr and s[i] == 'g':
            i += 1
            val += 1
        if val == 1:
            cnt = cnt
        elif val == 2:
            cnt = cnt * 2 % M
        else:
            val = fib(val + 1)
            cnt = cnt * val % M
    elif s[i] == 'f':
        val = 1
        i += 1
        while i < nr and s[i] == 'f':
            i += 1
            val += 1
        if val == 1:
            cnt = cnt
        elif val == 2:
            cnt = cnt * 2 % M
        else:
            val = fib(val + 1)
            cnt = cnt * val % M
    else:
        i += 1
print(cnt)
