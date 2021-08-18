def normalize(nested_list, growing_value=0):
    """Convert the given nested list to hypercube format with the given growing value and return it.
    """
    [dimension, size] = get_dimension_and_size(nested_list)
    return do_normalize(nested_list, dimension, size, growing_value)


def do_normalize(current_elem, dimension, size, growing_value):
    """Convert the given current element to hypercube format with the given dimension, size
        and growing value in a recursive manner.
    """
    is_basic = is_basic_element(current_elem)
    missing_element_count = size - len(current_elem) if not is_basic else size
    current_items = [] if is_basic else current_elem
    fill_value = current_elem if is_basic else growing_value

    return_elem = []
    if dimension > 1:
        for item in current_items:
            return_elem.append(do_normalize(item, dimension - 1, size, growing_value))
        for _ in range(missing_element_count):
            return_elem.append(
                do_normalize(fill_value, dimension - 1, size, growing_value)
            )
    else:
        return_elem = list(current_items)
        return_elem.extend(repeat_value(fill_value, missing_element_count))

    return return_elem


def get_dimension_and_size(nested_list, dimension=1):
    """Find out dimension and size for the given nested list
       * A nested list's dimension is defined as the deepest the list goes.
       * A nested list's size is defined as the longest the list or any of its sublists go.
    """
    dimensions = [dimension]
    sizes = [len(nested_list)]
    for list_item in nested_list:
        if not isinstance(list_item, list):
            continue
        [dim, size] = get_dimension_and_size(list_item, dimension + 1)
        dimensions.append(dim)
        sizes.append(size)
    return [max(dimensions), max(sizes)]


def is_basic_element(elem):
    return isinstance(elem, int)


def repeat_value(value, count):
    return [value for _ in range(count)]
