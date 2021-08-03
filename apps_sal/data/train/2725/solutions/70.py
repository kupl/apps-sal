def gimme(input_array):
    minEl = min(input_array)
    maxEl = max(input_array)
    i = 0
    for el in input_array:
        if el < maxEl and el > minEl:
            return i
        i = i + 1
