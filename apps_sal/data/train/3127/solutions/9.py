def string_chunk(string, n = None):
    if n > 0 and n != None and isinstance(n, int):
        return [string[i:i+n] for i in range(0, len(string), n)]
    else:
        return []
