def amicable_numbers(n1,n2):
    count_1 = 0
    count_2 = 0
    product = 0
    for i in range(1, n1):
        if n1 % i == 0:
            count_1 += i
    for i in range(1, n2):
        if n2 % i == 0:
            count_2 += i
    if n1 == count_2:
        product += 1
    if n2 == count_1:
        product += 1
    if product == 2:
        return True
    return False
