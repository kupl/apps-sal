def reverse_it(data):
    return data if any((t is type(data) for t in [dict, bool, list])) else type(data)(str(data)[::-1])
