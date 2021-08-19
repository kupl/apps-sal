def run_length_encoding(s):
    (count, prev, lst) = (1, '', [])
    for c in s:
        if c != prev:
            if prev:
                lst.append([count, prev])
            (count, prev) = (1, c)
        else:
            count += 1
    if len(prev) > 0:
        lst.append([count, prev])
    return lst
