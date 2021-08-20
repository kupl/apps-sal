import sys
readline = sys.stdin.readline
read = sys.stdin.read


def solve():
    s = input()
    n = len(s)
    if all((s[0] == k for k in s)):
        return 1
    somesame = 0
    for j in range(n - 1):
        if s[j] == s[j + 1]:
            somesame = 1
            break
    x = [(ord(i) - 1) % 3 for i in s]
    v = sum(x) % 3
    if n == 2:
        return 2
    if n == 3:
        if v == 0:
            return 3
        if somesame == 0:
            return 7
        else:
            return 6
    dp = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for _ in range(n - 1):
        ndp = [[0] * 3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if k == j:
                        continue
                    ndp[(i + k) % 3][k] += dp[i][j]
                    ndp[(i + k) % 3][k] %= MOD
        dp = ndp
    c = pow(3, n - 1, MOD)
    c -= sum(dp[v])
    if somesame == 0:
        c += 1
    return c % MOD


MOD = 998244353
print(solve())
'\ndef check(n):\n    from itertools import product\n    res = 0\n    for a in product(range(3),repeat=n):\n        for j in range(n-1):\n            if a[j] == a[j+1]: break\n        else:\n            continue\n        #print(a)\n        if sum(a)%3==0:\n            res += 1\n    print(res)\n\n\n\ndef check2(a):\n    n = len(a)\n    s = set()\n    s.add(tuple(a))\n    from random import randrange\n    for _ in range(2000):\n        co = a[:]\n        for k in range(1000):\n            i = randrange(0,n-1)\n            if co[i] != co[i+1]:\n                co[i] = co[i+1] = 2*(co[i]+co[i+1])%3\n            s.add(tuple(co))\n            if all(co[0] == k for k in co): break\n    print(a)\n    print(len(s),s)            \n\n\n            \ncheck(5)\n#check2([0,1,2,0,1,2])\n\n\n'
