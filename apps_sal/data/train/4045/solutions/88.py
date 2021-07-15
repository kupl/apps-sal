def number(lines):
    print(lines)
    if not lines:
        return lines
    lelist = []
    
    for c, value in enumerate(lines, 1):
        lelist.append(str(c) + ": " + value)
    
    return lelist
        
    #your code here

