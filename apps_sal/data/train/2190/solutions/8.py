from math import sqrt, ceil, gcd
from collections import defaultdict


def modInverse(b, m):
    g = gcd(b, m)
    if (g != 1):
        return -1
    else:
        return pow(b, m - 2, m)


def sol(n, m, rep):

    r = 1
    for i in range(2, n + 1):
        j = i
        while j % 2 == 0 and rep > 0:

            j //= 2
            rep -= 1

        r *= j
        r %= m

    return r


def solve():

    n = int(input())
    l = list(map(int, input().split()))
    st = []
    ans = 0
    hash = defaultdict(lambda: -1)
    for i in range(n):
        hash[i] = 0

        while st != [] and l[st[-1]] < l[i]:
            z = st.pop()
            hash[i] = max(hash[i], hash[z] + 1)

        if st == []:
            hash[i] = -1
        st.append(i)
        ans = max(ans, hash[i] + 1)
    print(ans)


solve()
