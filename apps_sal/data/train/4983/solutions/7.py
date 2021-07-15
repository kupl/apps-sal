def merge(*dicts):
    merged = {}
    
    for dict in dicts:
        for k, v in dict.items():
            merged.setdefault(k, []).append(v)
            
    return merged
