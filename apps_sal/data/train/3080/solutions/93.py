def who_is_paying(name):
    result = []
    if len(name) < 3:
        result.append(name)
        return result
    elif len(name) == 0:
        result.append('')
        return result
    result.append(name)
    result.append(name[:2])
    return result
