def get_function(sequence):
    slope = sequence[1] - sequence[0]
    for x in range(1,5):
        if sequence[x] - sequence[x-1] != slope:
            return "Non-linear sequence"
    
    return lambda a : slope * a + sequence[0]
