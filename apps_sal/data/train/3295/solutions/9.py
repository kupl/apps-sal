def split_in_parts(s, part_length):
    r = []
    for x in range(0, len(s), part_length):
        r += [s[x:x + part_length]]
    return ' '.join(r)
