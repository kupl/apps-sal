def string_chunk(string, n=None):
    if isinstance(n, int):
        if n > 0:
            return [string[i:i + n] for i in range(0, len(string), n)]
        else:
            return []
    else:
        return []
