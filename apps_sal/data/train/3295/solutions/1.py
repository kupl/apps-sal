def split_in_parts(s, n): 
    return ' '.join([s[i:i+n] for i in range(0, len(s), n)])
