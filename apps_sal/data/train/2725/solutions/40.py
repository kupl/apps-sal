def gimme(input_array):
    mi = min(input_array)
    ma = max(input_array)
    for i in range(len(input_array)):
        if input_array[i]!=mi and input_array[i] != ma:
            return i
