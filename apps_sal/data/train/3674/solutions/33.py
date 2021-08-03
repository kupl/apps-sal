def add_binary(a, b):
    output = ""
    result = a + b

    bit = 0x01

    while bit <= result:
        output = ("1" if (bit & result) > 0 else "0") + output
        bit *= 2

    return output
