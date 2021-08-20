from itertools import combinations_with_replacement
n = 201
s = [0] * n


def sieve(num):
    for i in range(1, num + 1):
        s[i] = i
    cd = [0 for i in range(num + 1)]
    for i in range(num + 1):
        cd[i] = 2
    for i in range(2, num + 1, 1):
        if s[i] == i and cd[i] == 2:
            for j in range(2 * i, num + 1, i):
                if cd[j] > 0:
                    s[j] = int(s[j] / i)
                    cd[j] -= 1
    res = []
    for i in range(2, num + 1, 1):
        if s[i] == 1 and cd[i] == 0:
            res.append(i)
    return res


t = int(input())
l = [int(input()) for i in range(t)]
count = 0
for i in l:
    a = sieve(i)
    c = list(combinations_with_replacement(a, 2))
    for j in c:
        if j[0] + j[1] == i:
            count += 1
            break
    if count > 0:
        print('YES')
    else:
        print('NO')
    count = 0
