def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in range(int(input())):
    (a, b) = map(int, input().split())
    if a or b:
        c = gcd(a, b)
        print(2 * c)
    else:
        print(0)
