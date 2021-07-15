def multiple_of_index(arr):
    return [elt for i, elt in enumerate(arr[1:]) if not elt % (i + 1)]
