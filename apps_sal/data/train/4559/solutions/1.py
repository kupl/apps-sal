def ones_complement(binary_number):
    return binary_number.translate(str.maketrans('01', '10'))
