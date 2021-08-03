n = int(input())


def getProduct(n):

    product = 1

    while (n != 0):
        product = product * (n % 10)
        n = n // 10

    return product


c = 0
cp = 0

for i in range(1, 1000000):
    count = 0
    s = str(i)
    for j in s:
        if j == '1':
            count += 1
    if count > 0 and getProduct(i) == n:
        cp += 1
    elif count == 0 and getProduct(i) == n:
        c += 1
print(c, cp)
