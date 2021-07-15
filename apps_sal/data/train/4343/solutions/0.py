def max_match(s):
    result = []
    
    while s:
        for size in range(len(s), 0, -1):
            word = s[:size]
            if word in VALID_WORDS:
                break
        
        result.append(word)
        s = s[size:]
    
    return result
