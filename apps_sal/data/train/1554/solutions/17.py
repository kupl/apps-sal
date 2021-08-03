# cook your dish here
def gcd(m, b):
    if m == 0:
        return b
    return gcd(b % m, m)


test = int(input())

while test != 0:
    m, b = list(map(int, input().split()))
    result = gcd(m, b)
    print(result * 2)
    test -= 1
