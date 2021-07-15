def run_length_encoding(s):
    ret = []
    p = None
    for c in s:
        if c == p:
            ret[-1][0] += 1
        else:
            ret.append([1, c])
            p = c
    return ret
