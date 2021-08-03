def strong_num(number):
    d = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return "STRONG!!!!" if number == sum([d[int(x)] for x in str(number)]) else "Not Strong !!"
