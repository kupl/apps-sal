def get_size(nested_list: List):
    size = len(nested_list)
    rank = 0
    for item in nested_list:
        if isinstance(item, list):
            (new_size, new_rank) = get_size(item)
            size = max(size, new_size)
            rank = max(rank, new_rank)
    return (size, 1 + rank)


def norm_list(item, rank, size, value):
    n_list = [item] * size if isinstance(item, int) else item + [value] * (size - len(item))
    rank = rank - 1
    if rank > 0:
        for idx in range(len(n_list)):
            n_list[idx] = norm_list(n_list[idx], rank, size, value)
    return n_list


def normalize(nested_list: List, growing_value: int = 0) -> List:
    (size, rank) = get_size(nested_list)
    return norm_list(nested_list, rank, size, growing_value)
