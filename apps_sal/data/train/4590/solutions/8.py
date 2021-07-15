def alt_or(lst):
    if len(lst) == 0:
        return None
    
    result = 0
    for boolean in lst:
        result += int(boolean)
    
    return bool(result)
