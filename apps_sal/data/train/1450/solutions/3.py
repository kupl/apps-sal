def gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


abc = 'abcdefghijklmnopqrstuvwxyz'
pi = 3.141592653589793
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = []
    for i in range(1, n + 1, 2):
        try:
            ans.append(arr[i])
        except:
            pass
        try:
            ans.append(arr[i - 1])
        except:
            pass
    print(*ans)
