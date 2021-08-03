CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def is_polydivisible(s, b):
    divide = 1
    if b == 10:
        while divide <= len(s):
            num = int(s[0:divide])
            if num % divide != 0:
                return False
            divide += 1
        return True
    else:
        while divide <= len(s):
            temp = divide
            index = 0
            num = 0
            while temp > 0:
                num += CHARS.index(s[index]) * (b**(temp - 1))
                temp -= 1
                index += 1
            if num % divide != 0:
                return False
            divide += 1
            num = 0
        return True


def get_polydivisible(n, b):
    count = 0
    count2 = 0
    temp = 1
    s = ""
    while True:
        if count2 >= b**temp:
            temp += 1
        record = count2
        power = temp
        while len(s) < temp:
            some = record // b**(power - 1)
            s += CHARS[some]
            record -= some * (b**(power - 1))
            power -= 1
        count2 += 1
        if is_polydivisible(s, b):
            count += 1
        if count == n:
            return s
        s = ""
