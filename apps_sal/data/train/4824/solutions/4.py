def get_min_max(seq): 
    return (min(seq),max(seq)) if len(seq)>1 else (seq[0],seq[0])
