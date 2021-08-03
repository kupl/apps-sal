def flip_bit(value, bit_index):
    binary = bin(value)[2:]

    if bit_index <= len(binary):
        lst = list(binary)
        lst[-bit_index] = "0" if binary[-bit_index] == "1" else "1"
        return int("".join(lst), 2)

    return value + 2**(bit_index - 1)
