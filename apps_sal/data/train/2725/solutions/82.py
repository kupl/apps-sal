def gimme(input_array):
    big = max(input_array)
    small = min(input_array)
    for num in input_array:
        if num > small and num < big:
            return input_array.index(num)
