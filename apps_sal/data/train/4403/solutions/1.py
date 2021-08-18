def switch_endian(n, bits):
    if not (0 <= n < 2**bits and bits == 2**(bits.bit_length() - 1)):
        return
    x = f"{n:0{bits}b}"
    return int(''.join(x[i - 8:i] for i in range(bits, 0, -8)), 2)
