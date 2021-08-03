# cook your dish here
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // (gcd(x, y))


abc = "abcdefghijklmnopqrstuvwxyz"

pi = 3.141592653589793238

n = int(input())
arr = list(map(int, input().split()))
revenue = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        cur = abs(arr[i] - arr[j])
        revenue += cur
print(revenue)
