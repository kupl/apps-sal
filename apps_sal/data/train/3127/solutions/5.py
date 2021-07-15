def string_chunk(s, n=0):
    return [s[i:i + n] for i in range(0, len(s), n)] if isinstance(n, int) and n > 0 else []
