def binary_cleaner(seq): 
    return [x for x in seq if x in [0, 1]], [i for i, x in enumerate(seq) if x > 1]
