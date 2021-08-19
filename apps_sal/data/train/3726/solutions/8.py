def sort_array(source_array):
    # Return a sorted array.
    odds = iter(sorted(elem for elem in source_array if elem % 2 != 0))
    return [next(odds) if el % 2 != 0 else el for el in source_array]
