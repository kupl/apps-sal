def to_twos_complement(binary, bits):
    binary = binary.replace(" ", "")
    sign_bit = binary[0]
    if sign_bit == "1":
        return int(binary[1:], 2) - 2**(bits - 1)
    else:
        return int(binary, 2)


def from_twos_complement(n, bits):
    print("new")
    if n >= 0:
        return format(n, 'b').zfill(bits)
    else:
        return format(2**bits + n, 'b')
