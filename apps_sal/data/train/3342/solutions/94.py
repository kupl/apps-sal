def pattern(n):
    pattern_string = ""
    
    for i in range(1, n + 1):
        for k in range(0, i):
            pattern_string = pattern_string + str(i)
        
        if i != n:
            pattern_string = pattern_string + '\n'
        
    return pattern_string
