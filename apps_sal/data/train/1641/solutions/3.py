def get_dim(obj, _cur_dim: int = 0) -> int:
    if not isinstance(obj, list):
        return _cur_dim
    elif len(obj) == 0:
        return _cur_dim + 1

    return max([get_dim(elem, _cur_dim + 1) for elem in obj])


def get_size(obj, _cur_size: int = 0) -> int:
    if not isinstance(obj, list) or len(obj) == 0:
        return 0

    return max([len(obj), max([get_size(elem) for elem in obj])])


def _generate_for_value(value, size: int, dim: int):
    if dim == 1:
        return [value] * size

    return [_generate_for_value(value, size, dim - 1)] * size


def _normalize(obj, size: int, dim: int, growing_value: int):
    if not isinstance(obj, list):
        return _generate_for_value(obj, size, dim)

    if len(obj) == 0:
        return _generate_for_value(growing_value, size, dim)

    grow = size - len(obj)
    obj = obj + [growing_value] * grow

    if dim == 1:
        return obj

    return [_normalize(elem, size, dim - 1, growing_value) for elem in obj]


def normalize(nested_list: List, growing_value: int = 0) -> List:
    """Convert the given nested list to hypercube format with the given <growing_value> and return it.
    """
    size = get_size(nested_list)
    dim = get_dim(nested_list)
    return _normalize(nested_list, size, dim, growing_value)
