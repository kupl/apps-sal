def gimme(input_array):
    srt = sorted(input_array)
    for i in range(3):
        if input_array[i] == srt[1]:
            return i
