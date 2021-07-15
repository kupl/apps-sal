def flatten(*args):
    flattened_list = [arg for arg in args]
    result = []
    while any(isinstance(element, list) for element in flattened_list):
        for element in flattened_list:
            if type(element) is list:
                for j in element:
                    result.append(j)
            else:
                result.append(element)
        flattened_list = result[:]
        result.clear()
    return flattened_list
