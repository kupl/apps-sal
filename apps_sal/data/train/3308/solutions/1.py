def parity_bit(binary):
    return " ".join("error" if byte.count("1") & 1 else byte[:-1] for byte in binary.split())
