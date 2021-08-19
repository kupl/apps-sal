def simplify(path):
    array = [(0, 0)]
    for elem in path:
        if elem == '^':
            array.append((array[-1][0], array[-1][1] + 1))
        elif elem == 'v':
            array.append((array[-1][0], array[-1][1] - 1))
        elif elem == '>':
            array.append((array[-1][0] + 1, array[-1][1]))
        else:
            array.append((array[-1][0] - 1, array[-1][1]))
    for i in range(0, len(array) - 1):
        for j in range(len(array) - 1, i + 1, -1):
            if array[i] == array[j]:
                array = array[:i] + [None for i in range(j - i)] + array[j:]
    res = [path[i] for i in range(len(path)) if array[i] is not None]
    return ''.join(res)
