
def insert_dash(num):
    def odd(c):
        return not (ord(c) & 1 ^ 1)
    a = []
    for digit in str(num):
        if odd(digit) and a and odd(a[-1]):
            a.append('-')
        a.append(digit)
    return "".join(a)
