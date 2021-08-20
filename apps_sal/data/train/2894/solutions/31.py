def triple_trouble(one, two, three):
    x = list(zip(one, two, three))
    result = []
    for item in x:
        result.append(''.join(item))
    return ''.join(result)
