# return a sorted set with the difference
def diff(a, b):
    output = []
    for elem in a:
        if elem not in b:
            output.append(elem)
    for elem in b:
        if elem not in a:
            output.append(elem)
    return sorted(list(set(output)))
