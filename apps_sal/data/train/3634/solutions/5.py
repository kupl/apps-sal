def reverse_it(data):
    return data[::-1] if isinstance(data, str) else int(str(data)[::-1]) if isinstance(data, int) and not isinstance(data, bool) else float(str(data)[::-1]) if isinstance(data, float) else data
