def complete_series(seq): 
    return list(range(1 + (len(seq) == len(set(seq)) and max(seq))))
