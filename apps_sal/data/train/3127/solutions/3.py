def string_chunk(xs, n=None):
    try:
        return [xs[i:i + n] for i in range(0, len(xs), n)]
    except:
        return []
