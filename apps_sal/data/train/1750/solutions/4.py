def dec_to_bin(num):
    if num <= 0:
        return '0'

    bits = ''
    while num > 0:
        bits = str(num % 2) + bits
        num = num / 2

    return bits


def bin_to_dec(binary):
    dec = 0
    power = 0
    for b in reversed(binary):
        dec += int(b) * 2 ** power
        power += 1

    return dec


def mystery(num):
    b = dec_to_bin(num)
    out = ''
    reverse = False
    for bit in b:
        if not reverse:
            out += bit
        else:
            out += '0' if bit == '1' else '1'

        reverse = not reverse if out[-1] == '1' else reverse

    return bin_to_dec(out)


def mystery_inv(num):
    if num == 0:
        return num

    b = dec_to_bin(num)
    out = ''
    reverse = b[0] == '0'
    for bit in b:
        if not reverse:
            out += bit
        else:
            out += '0' if bit == '1' else '1'

        reverse = not reverse if bit == '1' else reverse

    return bin_to_dec(out)


def name_of_mystery():
    return 'Gray code'
