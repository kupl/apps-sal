def gap(num):
    binary = bin(num)[2:]
    gaps = binary.strip("0").split("1")
    return len(max(gaps))
