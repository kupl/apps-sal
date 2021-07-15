def complete_series(seq): 
    # your code here
    seq.sort()
    if len(seq) == len(set(seq)):
        return [number for number in range(seq[-1]+1)]
    else:
        return [0]
