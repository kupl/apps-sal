def complete_series(seq): 
    return [0] if len(set(seq)) < len(seq) else list(range(0,max(seq)+1))
