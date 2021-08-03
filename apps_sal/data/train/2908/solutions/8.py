def flatten(dictionary):
    stack = [("", dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        if current:
            if type(current) == dict:
                if path:
                    path += '/'
                for key in current:
                    stack.append((path + key, current[key]))
            else:
                result[path] = current
        elif path:
            result[path] = ""
    return result
