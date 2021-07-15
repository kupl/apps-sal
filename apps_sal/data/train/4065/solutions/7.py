def get_sequence(offset, size):
    result = []
    if offset < 1023456789:
        offset = 1023456789
    while len(result) < size and offset < 10000000000:
        if len(set(str(offset))) == 10:
            result.append(offset)
        offset += 1
    return result
