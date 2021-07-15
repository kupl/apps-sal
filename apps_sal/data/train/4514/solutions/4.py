def int_to_negabinary(i):
    digits = []
    if not i:
        digits = ['0']
    else:
        while i != 0:
            i, remainder = divmod(i, -2)
            if remainder < 0:
                i, remainder = i + 1, remainder + 2
            digits.append(str(remainder))
    return ''.join(digits[::-1])
    
def negabinary_to_int(s):
    num = 0
    for c in s:
        num *= -2
        num += ('01').find(c)
    return num

