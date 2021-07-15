def split_in_parts(stg, size): 
    return " ".join(stg[i:i+size] for i in range(0, len(stg), size))
