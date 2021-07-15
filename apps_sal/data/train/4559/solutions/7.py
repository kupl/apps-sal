def ones_complement(binary):
    return "".join("01"[b=="0"] for b in binary)
