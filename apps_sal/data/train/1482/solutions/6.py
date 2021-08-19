def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


t = int(input())


def isPalindrome(n: int) -> bool:
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
    return n == rev


for _ in range(t):
    n = int(input())
    p = 9
    tot = 9
    q = 0
    flag = 0
    num = 0
    if n == 1:
        print(1, end=' ')
        flag = 1
        print(1)
    else:
        for i in range(2, n + 1):
            if i % 2 == 0:
                pass
            else:
                p *= 10
    if flag == 0:
        q = 10 ** n - 10 ** (n - 1)
        print(str(p // gcd(p, q)) + ' ' + str(q // gcd(p, q)))
