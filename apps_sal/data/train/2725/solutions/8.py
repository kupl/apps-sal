import copy


def gimme(input_array):
    input_array_sorted = copy.deepcopy(input_array)
    input_array_sorted.sort()
    middle = input_array_sorted[int(len(input_array_sorted) / 2)]
    return input_array.index(middle)
