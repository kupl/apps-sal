def positive_to_negative(binary):
    return [1 - d if 1 in binary[i:] else d for (i, d) in enumerate(binary, 1)]
