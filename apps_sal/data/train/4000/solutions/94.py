from math import factorial as f


def strong_num(number):
    s = sum(f(int(x)) for x in str(number))
    return "STRONG!!!!" if number == s else "Not Strong !!"
