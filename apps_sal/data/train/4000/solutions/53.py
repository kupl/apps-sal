def strong_num(number):
    sum = 0
    for i in str(number):
        a = 1
        j = 1
        while j < int(i) + 1:
            a *= j
            j += 1
        sum += a
    if sum == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
