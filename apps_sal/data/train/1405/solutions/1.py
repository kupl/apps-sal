from math import sqrt
t = int(input())


def isprime(n):

    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


d = {}
for i in range(2, 100000):
    d[i] = isprime(i)
l = [i for i in d.keys() if d[i] == True]
for _ in range(t):
    n = int(input())
    s = 0
    e = len(l) - 1
    ans = -1
    while(s <= e):
        mid = (s + e) // 2
        if((l[mid]**4) <= n):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    print(ans + 1)
