def strong_num(number):
    sum1 = 0
    for i in str(number):
        num = 1
        a = int(i)
        for i in range(1, a + 1):
            num = num * i
        sum1 += num
    if number == sum1:
        return "STRONG!!!!"
    return "Not Strong !!"
