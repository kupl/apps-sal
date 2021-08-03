def merge_arrays(first, second):
    final = first + second
    final.sort()
    return list(dict.fromkeys(final))
