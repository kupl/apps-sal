def decimalToBinary(n):
    return bin(n).replace("0b", "")


def bin_mul(m, n):
    Binval = m
    Top = n
    if m < n:
        Binval = n
        Top = m
    Binary = list(decimalToBinary(Binval))
    val = []
    Binary.reverse()
    for x in Binary:
        if int(x) == 1 and Top != 0:
            val.append(int(x) * Top)
        Binval -= int(abs(Binval / 2))
        Top *= 2
    return val[::-1]
