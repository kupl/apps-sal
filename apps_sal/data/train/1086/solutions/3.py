mod = 10**9 + 7
def gcd(a,b): return b and gcd(b, a % b) or a

def fac50():
    f = [0]*51
    f[0] = 1
    f[1] = 1
    for i in range(1,51):
        f[i] = (f[i-1]*i)%mod
    return f

def gcd110():

    gc = [[0]*111 for i in range(111)]
    for i in range(111):
        for j in range(111):
            gc[i][j] = gcd(i,j)
    return gc

factorials = fac50()
gcds = gcd110()

def rule_asc(n,l):
    a = [0 for i in range(n + 1)]
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y and k < l - 1:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        yield a[:k + 1]

def niceness(s):
    t = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            t = (t + gcds[s[i]][s[j]])%mod
    return t


def permcount(s,c):
    f = [s.count(x) for x in set(s)]
    p = factorials[c]
    for e in f:
        p = (p*pow(factorials[e],mod-2,mod))%mod
    return p

def main():

    t  = int(input())

    for i in range(t):

        n,s = [int(item) for item in input().split()]
        a = [int(item) for item in input().split()]
        b = [i for i in a if i != -1]
        s -= sum(b)
        ones = a.count(-1)

        if s < 0:
            print(0)
        elif (s == 0 and ones == 0):
            print(niceness(a)%mod)
        elif (s > 0 and ones == 0):
            print(0)
        else:

            t = 0
            for seq in rule_asc(s,ones):
                if len(seq) == ones:
                    p = permcount(seq,ones)
                    t = (t + ((p%mod)*(niceness(b+seq)%mod))%mod)%mod

            print(t)

def __starting_point():
    main()

__starting_point()
