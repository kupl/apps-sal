def array_info(x):
    if len(x) == 0:
        return 'Nothing in the array!'
    info = [[len(x)], [sum((1 for y in x if isinstance(y, int)))], [sum((1 for y in x if isinstance(y, float)))], [sum((1 for y in x if isinstance(y, str) and y != ' '))], [sum((1 for y in x if y == ' '))]]
    for (j, i) in enumerate(info):
        if i == [0]:
            info[j] = [None]
    return info
