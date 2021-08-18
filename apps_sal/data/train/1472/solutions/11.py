def getProduct(n):
    product = 1

    while (n != 0):
        product = product * (n % 10)
        n = n // 10

    return product


special = 0
partially = 0
n = int(input())
for i in range(1, (10**6) + 1):
    if getProduct(i) == n:
        str_i = str(i)
        if str_i.count("1") > 0:
            partially += 1
        else:
            special += 1
print(special, partially)
