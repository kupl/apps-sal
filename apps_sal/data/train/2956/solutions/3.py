def encode(string):
    values = "".join(format(x, "08b") for x in map(ord, string))
    return values.replace("0", "000").replace("1", "111")


def decode(bits):
    bs = "".join("0" if xs.count("0") >= 2 else "1" for xs in zip(*[iter(bits)] * 3))
    return "".join(chr(int("".join(b), 2)) for b in zip(*[iter(bs)] * 8))
