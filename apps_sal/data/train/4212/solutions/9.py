def unite_unique(*args):
    result = []
    [[result.append(nr) for nr in arg if nr not in result] for arg in args]
    return result
