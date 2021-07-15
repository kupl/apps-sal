def ones_complement(binary_number):
    return "".join([ "1" if binary_number[x] == "0" else "0" for x in range(0, len(binary_number))])
