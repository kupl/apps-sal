# convert binary
def convert_bin(arr):
    summa = 0
    for x, y in enumerate(arr[::-1]):
        summa = summa + 2**x * int(y)
    return summa


def int32_to_ip(int32):

    n = ""

    while int32 > 0:
        y = str(int32 % 2)
        n = y + n
        int32 = int(int32 / 2)

    if len(n) != 32:  # make 32 bit
        while len(n) != 32:
            n = '0' + n

    a = n[:8]  # first 8
    b = n[8:16]  # secound 8
    c = n[16: 24]  # third 8
    d = n[24: 32]  # fourth 8

    return(str(convert_bin(a)) + '.' + str(convert_bin(b)) + '.' + str(convert_bin(c)) + '.' + str(convert_bin(d)))
