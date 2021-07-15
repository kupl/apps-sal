def string_chunk(string, n=0):
    return [string[i:i+n] for i in range(0,len(string), n)] if isinstance(n, int) and n > 0 else []

