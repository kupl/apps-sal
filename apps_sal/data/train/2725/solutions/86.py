def gimme(input_array):
    M = max(input_array)
    m = min(input_array)
    if input_array.index(M) == 2 and input_array.index(m) == 0:
        return 1
    if input_array.index(M) == 1 and input_array.index(m) == 0:
        return 2
    if input_array.index(M) == 1 and input_array.index(m) == 2:
        return 0
    if input_array.index(M) == 2 and input_array.index(m) == 1:
        return 0
    if input_array.index(M) == 0 and input_array.index(m) == 2:
        return 1
    if input_array.index(M) == 0 and input_array.index(m) == 1:
        return 2
