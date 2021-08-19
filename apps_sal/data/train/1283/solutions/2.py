# cook your dish here
def AlmostPrime(n):
    pf = []
    while n % 2 == 0:
        n //= 2
        pf.append(2)
    k = 3
    while k <= n:
        while n % k == 0:
            n //= k
            pf.append(k)
        k += 2
    return len(pf) == 2 and pf[0] != pf[1]


def semi_prime(n):
    for i in range(6, n // 2 + 1):
        if AlmostPrime(i) and AlmostPrime(n - i):
            # print(i,n-i)
            return "YES"
    return "NO"


for _ in range(int(input())):
    print(semi_prime(int(input())))
