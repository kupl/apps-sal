from collections import Iterable


def unpack(xs):
    queue = xs[:]
    output = []
    while queue:
        x = queue.pop(0)
        if type(x) is dict:
            queue.append(x.items())
        elif type(x) != str and isinstance(x, Iterable):
            queue.extend(x)
        else:
            output.append(x)
    return output
