def merge_arrays(first, second): 
    final = set()
    for i in first:
        final.update(first)
        final.update(second)
    return sorted(final)
