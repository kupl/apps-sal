def split_in_parts(s, part_length):
    new = ''
    i = 0
    for x in s:
        if i == part_length:
            new += ' '
            new += x
            i = 1
        else:
            new += x
            i += 1
    return new
