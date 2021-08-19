def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        (path, current) = stack.pop()
        for (k, v) in current.items():
            if v == {}:
                result['/'.join(path + (k,))] = ''
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result['/'.join(path + (k,))] = v
    return result
