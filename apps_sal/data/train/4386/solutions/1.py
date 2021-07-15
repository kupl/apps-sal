def is_in_middle(seq):
    mid, rem = divmod(len(seq), 2)
    start = mid-1
    end = start+3
    
    if not rem: 
        start -= 1
    
    return 'abc' in seq[start:end]

