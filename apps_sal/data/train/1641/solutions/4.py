from itertools import zip_longest


def normalize(nested_list, growing_value=0):
    dimension, size = list(map(max, list(zip(*get_dimension_and_size(nested_list)))))
    return do_normalize(nested_list, dimension, size, growing_value)


def get_dimension_and_size(nested_list, dimension=1):
    yield dimension, len(nested_list)
    for list_item in nested_list:
        if isinstance(list_item, list):
            yield from get_dimension_and_size(list_item, dimension + 1)


def do_normalize(nested_list, dimension, size, growing_value):
    return_list = []

    for list_item, _ in zip_longest(nested_list, list(range(size)), fillvalue=growing_value):
        if dimension > 1:
            list_to_normalize = (
                list_item if isinstance(list_item, list) else [list_item] * size
            )
            return_list.append(
                do_normalize(list_to_normalize, dimension - 1, size, growing_value)
            )
        else:
            return_list.append(list_item)

    return return_list
