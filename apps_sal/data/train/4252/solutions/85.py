def merge_arrays(first, second):
    first_set = set(first)
    second_set = set(second)
    inter = first_set.intersection(second_set)
    unio = first_set.union(second_set)
    my_list = list(unio)
    return sorted(my_list)
