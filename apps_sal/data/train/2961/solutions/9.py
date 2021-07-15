def complete_series(seq): 
    if len(seq) != len(set(seq)):
        return [0]
    return list(range(max(seq)+1))
