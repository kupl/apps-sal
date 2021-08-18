def disarium_number(number):
    m = 10
    i = 10
    result = 0
    count = 1
    once = True
    a = None
    zero_count = 0
    while count > 0:
        if int(number / i) != 0:
            if number % i == 0:
                a = int(number / i)
                zero_count += 1
            i *= 10
            count += 1
        else:
            if a is not None:
                number = a
                count = count - zero_count
                i = 10 ** count
            j = count
            for q in range(j + 1):
                k = (number * (m ** count)) / i
                p = int(((k / 10) % 1) * 10)
                if once and number % 2 != p % 2:
                    p += 1
                    once = False
                once = False
                result += p ** count
                count -= 1
                if count < 1:
                    break
    if number == result:
        return "Disarium !!"
    return "Not !!"
