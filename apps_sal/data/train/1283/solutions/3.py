def seive_array():
    n = 200
    seive = [1] * (n + 1)
    seive[0] = 0
    seive[1] = 0
    i = 2
    while i * i <= n:
        if seive[i] == 1:
            for j in range(i * i, n + 1, i):
                seive[j] = 0
        i += 1
    return seive


def check_semi_prime(x):
    k = 2
    p1 = 0
    p2 = 0
    while k < x:
        if x % k == 0 and seive[k] == 1:
            p1 = k
        if x == p1 * p2 and p1 != p2:
            return 1
        else:
            p2 = p1
            k += 1
    return 0


def given_number(m):
    for i in range(2, m // 2 + 1):
        x = i
        y = m - x
        if check_semi_prime(x) and check_semi_prime(y):
            return 1


t = int(input())
seive = seive_array()
for i in range(t):
    m = int(input())
    if given_number(m):
        print('YES')
    else:
        print('NO')
