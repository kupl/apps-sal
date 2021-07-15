def get_sequence(offset, size):
    i, re = 1023456789 if offset < 1023456789 else offset, []
    while i <= 9876543210 and len(re) < size:
        if sorted('0123456789') == sorted(str(i)):
            re.append(i)
        i += 1
    return re
