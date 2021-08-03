def add_binary(a, b):
    sum1 = int(a + b)
    i = 0
    str1 = ""
    if sum1 == 0:
        str1 = '0'
    while sum1 != 0:
        rem = int(sum1 % 2)
        str1 = str(rem) + str1
        sum1 = int(sum1 // 2)
    return str1
