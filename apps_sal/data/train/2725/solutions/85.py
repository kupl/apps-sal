def gimme(input_array):
    Max = max(input_array)
    Min = min(input_array)
    n = round(sum(input_array), 3)
    k = round(n - Max - Min, 3)
    return input_array.index(k)
