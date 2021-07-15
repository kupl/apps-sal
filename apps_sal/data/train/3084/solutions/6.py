def combine(*args):
    result = {}
    for obj in args:
        for key, value in obj.items():
            if not key in result:
                result[key] = 0
            result[key] += value
    return result
