def string_chunk(string, n=0):
    if isinstance(n, int) and n > 0:
        starts = range(0, len(string), n)
    else:
        starts = []
    return [string[i:i + n] for i in starts]
