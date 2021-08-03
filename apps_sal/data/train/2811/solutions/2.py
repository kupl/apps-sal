from itertools import groupby


def send(stg):
    bits = "".join(f"{ord(c):07b}" for c in stg)
    return " ".join(f"{'0' * (2 - int(b))} {'0' * len(tuple(l))}" for b, l in groupby(bits))


def receive(stg):
    chunks = stg.split()
    bits = zip(chunks[::2], chunks[1::2])
    chars = "".join(f"{2 - len(bit)}" * len(length) for bit, length in bits)
    return "".join(chr(int(chars[i:i + 7], 2)) for i in range(0, len(chars), 7))
