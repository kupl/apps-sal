def merge_arrays(first, second):
    new_list = first + second
    new_list.sort()

    return list(dict.fromkeys(new_list))
