def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in list(current.items()):
            new_path = path + (k,)
            v = v if v else ""
            if isinstance(v, dict):
                stack.append((new_path, v))
            else:
                result["/".join(new_path)] = v
    return result

