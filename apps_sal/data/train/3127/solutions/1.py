def string_chunk(s, n=0):
    if not isinstance(n, int) or n == 0:
        return []
    return [s[i:i + n] for i in range(0, len(s), n)]
