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


n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()
x = False
for i in range(n):
    if(arr1[i] != arr2[i]):
        print(arr2[i])
        x = True
        break


if(not x):
    print(arr2[-1])
