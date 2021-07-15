def binary_to_string(binary):
    return int(binary, 2).to_bytes(len(binary)//8, "big").decode() if binary else binary
