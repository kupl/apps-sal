def get_sequence(offset, size):
    out = []
    if offset < 1023456789:
        offset = 1023456789
    while len(out) < size and offset < 9876543211:
        if sorted(str(offset)) == ['0','1','2','3','4','5','6','7','8','9']:
            out.append(offset)
        offset += 1
    return out


