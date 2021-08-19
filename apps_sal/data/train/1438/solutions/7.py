p = 10 ** 6 + 5


def Sieve():
    l = [True] * p
    s = [0] * p
    for i in range(2, p):
        if l[i]:
            for j in range(i, p, i):
                s[j] += i
                l[j] = False
        i += 1
    l[0] = l[1] = False
    return (l, s)


(isprime, s) = Sieve()
for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    c = 0
    for i in range(n):
        for j in range(n):
            if s[l[j]] % s[l[i]] == 0 and l[j] % l[i] == 0 and (i != j):
                c += 1
    print(c)
