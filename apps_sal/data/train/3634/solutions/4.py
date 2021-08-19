def reverse_it(data):
    return type(data)(str(data)[::-1]) if isinstance(data, (str, int, float)) else data
