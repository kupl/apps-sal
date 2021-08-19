def int_to_negabinary(n):

    def do(n1):
        li = []
        while n1 != 0:
            li.append(str(abs(n1 % -2)))
            n1 //= -2
        return li[::-1]
    return ''.join([do(abs(n)), do(-n)][n > 0]) or '0'


def negabinary_to_int(n):
    return sum([int(j) * (-2) ** i for (i, j) in enumerate(n[::-1])])
