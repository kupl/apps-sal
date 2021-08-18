def normalize(nested_list: List, growing_value: int = 0) -> List:
    """Convert the given nested list to hypercube format with the given <growing_value> and return it.
    """
    return extend(nested_list, dimension(nested_list), size(nested_list), growing_value)


def extend(nl, dimension, size, growing_value):
    if dimension == 1:
        try:
            s = len(nl)
        except TypeError:
            return [nl] * size
        return nl + [growing_value] * (size - s)
    try:
        s = len(nl)
    except TypeError:
        return [extend(nl, dimension - 1, size, growing_value)] * size
    else:
        return ([extend(sl, dimension - 1, size, growing_value) for sl in nl] +
                [extend(growing_value, dimension - 1, size, growing_value)] * (size - s))


def dimension(nested_list):
    try:
        return 1 + max((dimension(l) for l in nested_list), default=0)
    except TypeError:
        return 0


def size(nested_list):
    try:
        d = len(nested_list)
    except TypeError:
        return 0
    return max(d, max((size(l) for l in nested_list), default=0))
