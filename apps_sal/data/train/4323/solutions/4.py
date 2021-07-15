def uniq(seq): 
    return ([seq[0]] + [seq[i] for i in range(1, len(seq)) if seq[i] != seq[i-1]] if seq else [])
