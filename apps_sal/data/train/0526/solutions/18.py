def fac(a):
    s = 1
    for i in range(1, a + 1):
        s = s * i
    return s


def prime(n):
    n = int(n)
    if(n == 2 or n == 3):
        return 1
    k = n**(1 / 2)
    for i in range(2, int(k) + 2):
        if(n % i == 0):
            return 0
    return 1


def sieve(n):
    arr = []
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            arr.append(p)
    return arr


t = int(input())
# n,m=[int(x) for x in input().split()]

for ii in range(t):
    s = input()
    prev = s[0]
    ss = []
    c = 1
    for i in s[1:]:
        if(i != prev):
            if(c == 1):
                ss.append('p' + prev)
            else:
                ss.append('p' + prev)
                ss.append(str(c))
            prev = i
            c = 1
        else:
            c += 1

    if(c == 1):
        ss.append('p' + prev)
    else:
        ss.append('p' + prev)
        ss.append(str(c))
    hah = '0987654321'
    s1 = 0
    s2 = 0

    s1 = 8 * (len(s))
    for i in ss:
        if (i[0] in hah):
            s2 += 32
        else:
            s2 += 8
    # print(s,ss)
    print(s1 - s2)
