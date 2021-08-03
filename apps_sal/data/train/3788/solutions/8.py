from decimal import Decimal


def g_p_num(n):
    return isqrt(1 + 24 * n) >= 0


def isqrt(n):
    sqrt = Decimal(n).sqrt()
    i = int(sqrt)
    if i == sqrt:
        return i
    return -1


def s_p_num(n):
    return n in {1, 9801, 94109401, 903638458801, 8676736387298001, 83314021887196947001, 799981229484128697805801, 7681419682192581869134354401, 73756990988431941623299373152801, 708214619789503821274338711878841001, 6800276705461824703444258688161258139001}


def p_num(n):
    d = isqrt(1 + 24 * n)
    return d >= 0 and (int(d) + 1) % 6 == 0
