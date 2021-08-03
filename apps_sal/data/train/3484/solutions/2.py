def time_convert(num):
    a = num // 60
    b = num % 60
    if num <= 0:
        return '00:00'
    elif 0 < num < 10:
        return '00:0' + str(num)
    elif 10 <= num < 60:
        return '00:' + str(num)
    else:
        if a < 10 and b < 10:
            return "0" + str(a) + ':' + "0" + str(b)
        elif a >= 10 and b < 10:
            return str(a) + ':' + "0" + str(b)
        elif a < 10 and b >= 10:
            return "0" + str(a) + ':' + str(b)
        elif a >= 10 and b >= 10:
            return str(a) + ':' + str(b)
