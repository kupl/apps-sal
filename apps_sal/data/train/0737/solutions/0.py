from math import sqrt


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0):
            return True
    return False


ans = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    ans.append('NO' if(isPrime(x**2 - y**2)) else 'YES')
print('\n'.join(ans))
