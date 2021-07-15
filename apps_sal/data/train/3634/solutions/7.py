def reverse_it(data):
    return type(data)(str(data)[::-1]) if type(data) in (str, int, float) else data
