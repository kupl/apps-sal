""" codewars - Hypercube lists """


def longest_len(arr: list):
    """ longst len in a list of list-things """
    list_lens = []
    list_lens.append(len(arr))

    for curr_l in arr:
        if isinstance(curr_l, list):
            list_lens.append(len(curr_l))
            list_lens.append(longest_len(curr_l))
    return max(list_lens) if list_lens else 0


def deepest_depth(arr: list, current_depth: int = 1):
    """ returns the deepest depth """
    depths = []

    for item in arr:
        if isinstance(item, int):
            depths.append(current_depth)
        elif isinstance(item, list):
            depths.append(deepest_depth(item, current_depth + 1))
    return max(depths) if depths else current_depth


def deep_copy(nested_list: list) -> list:
    """ returns a copy """
    res = []
    for item in nested_list:
        if isinstance(item, int):
            res.append(item)
        elif isinstance(item, list):
            res.append(deep_copy(item))
    return res


def normalize(nested_list: list, growing_value: int = 0) -> list:
    """ does tha thing """
    working_list = deep_copy(nested_list)
    target_length = longest_len(working_list)
    target_depth = deepest_depth(working_list)
    extendify(
        working_list,
        target_depth,
        target_length,
        fill_value=growing_value)
    # print(len(working_list))
    return working_list


def extendify(arr: list, target_depth: int, target_length: int,
              depth: int = 1, fill_value: int = 0):
    """ extendifies an arr """

    arr.extend([fill_value] * (target_length - (len(arr))))

    if depth < target_depth:
        for i, current_item in enumerate(arr):
            if isinstance(current_item, int):
                arr[i] = extendify(
                    [],
                    target_depth,
                    target_length,
                    depth + 1,
                    fill_value=current_item)
            elif isinstance(current_item, list):
                arr[i] = extendify(
                    current_item,
                    target_depth,
                    target_length,
                    depth + 1,
                    fill_value=fill_value)
    return arr


