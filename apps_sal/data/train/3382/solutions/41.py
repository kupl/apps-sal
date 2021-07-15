def lowercase_count(strng):
    # Your code here
    import re
    from re import finditer
    
    pattern = r"[a-z]"
    
    count = 0
    
    for it in finditer(pattern,strng):
        count += 1
    
    return count
