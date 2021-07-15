def string_chunk(string, n=None):
    ret = []
    if isinstance(n, int) and n > 0:
        for i in range(0, len(string), n):
            ret.append(string[i:i+n])
    return ret
