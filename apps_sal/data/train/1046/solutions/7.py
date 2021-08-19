# cook your dish here
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // (gcd(x, y))


def isPrime(n):
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


abc = "abcdefghijklmnopqrstuvwxyz"

pi = 3.141592653589793238

#n = int(input())
#arr = list(map(int,input().split()))

t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    i = 1
    while(1):
        a = a - i
        if(a < 0):
            flag = False
            break
        i = i + 1
        b = b - i
        if(b < 0):
            flag = True
            break
        i = i + 1

    if(not flag):
        print('Bob')
    else:
        print('Limak')


# Output:
# Bob
# Limak
# Limak
# Bob
# Bob
# Limak
# Limak
# Bob
# Bob
# Bob
