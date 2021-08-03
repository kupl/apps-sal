def to_twos_complement(binary, bits):
    binary = "".join(binary.split())
    res = -(2**(bits - 1)) if binary[0] == "1" else 0
    for i in range(1, bits):
        res += 2**(bits - 1 - i) if binary[i] == "1" else 0
    return res


def from_twos_complement(n, bits):
    if n >= 0:
        return "0" * (bits - len(bin(n)[2:])) + bin(n)[2:]
    else:
        remain = abs(-(2**(bits - 1)) - n)
        return "1" + "0" * (bits - len(bin(remain)[2:]) - 1) + bin(remain)[2:]
