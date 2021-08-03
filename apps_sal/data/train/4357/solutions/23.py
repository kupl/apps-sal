def nth_smallest(arr, pos):
    x = sorted(arr)
    steps = 1
    for i in x:
        if steps == pos:
            return i
        else:
            steps += 1
