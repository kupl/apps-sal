def unite_unique(*args):
    result = []
    for e in sum(args, []):
        if e not in result:
            result.append(e)
    return result
