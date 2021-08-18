def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


t = int(input())
for i in range(t):
    temp = input().split()
    n = int(temp[0])
    a = int(temp[1])
    k = int(temp[2])
    tempn = (n - 2) * 180
    tempn = tempn * 2
    tempd = n
    tempn = tempn - 2 * a * tempd
    tempd = tempd * (n - 1)
    tempn = tempn * (k - 1) + a * tempd
    g = gcd(tempn, tempd)
    tempn /= g
    tempd /= g
    print(int(tempn), int(tempd))
