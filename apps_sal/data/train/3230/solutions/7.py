def the_biggest_search_keys(*keys):
    if not keys:
        return "''"
    
    max_len = 0
    
    for key in keys:
        key_len = len(key)
        
        if key_len > max_len:
            max_len = key_len
            result = [key]
        
        elif key_len == max_len:
            result += [key]
    
    return str( sorted(result) )[1:-1]
