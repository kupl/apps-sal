def nth_smallest(arr, pos):

    arr.sort()

    for i, j in enumerate(arr, 1):

        if i == pos:

            return j
