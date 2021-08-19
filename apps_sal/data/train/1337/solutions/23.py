# cook your dish here
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) // gcd(a, b)


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    if(n == 1):
        print(arr[0] + k)
    if(n == 2):
        print(lcm(arr[0], arr[1]) + k)
    else:
        l = lcm(arr[0], arr[1])
        for i in range(2, len(arr)):
            l = lcm(l, arr[i])
        print(l + k)
