def merge_arrays(first, second):
    mylist = first + second
    return sorted(list(dict.fromkeys(mylist)))
