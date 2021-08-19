# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read


def solve():
    s = input()
    n = len(s)
    if all(s[0] == k for k in s):
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
        # for c in dp:
        #    print(3**(_+1) - sum(c), end = " ")
        # print(dp)

    c = pow(3, n - 1, MOD)
    c -= sum(dp[v])
    if somesame == 0:
        c += 1
    return c % MOD


MOD = 998244353
print(solve())


"""
def check(n):
    from itertools import product
    res = 0
    for a in product(range(3),repeat=n):
        for j in range(n-1):
            if a[j] == a[j+1]: break
        else:
            continue
        #print(a)
        if sum(a)%3==0:
            res += 1
    print(res)



def check2(a):
    n = len(a)
    s = set()
    s.add(tuple(a))
    from random import randrange
    for _ in range(2000):
        co = a[:]
        for k in range(1000):
            i = randrange(0,n-1)
            if co[i] != co[i+1]:
                co[i] = co[i+1] = 2*(co[i]+co[i+1])%3
            s.add(tuple(co))
            if all(co[0] == k for k in co): break
    print(a)
    print(len(s),s)            


            
check(5)
#check2([0,1,2,0,1,2])


"""
