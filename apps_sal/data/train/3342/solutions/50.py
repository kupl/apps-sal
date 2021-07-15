def pattern(n):
    d = []
    for i in range(n):
        counter = i+ 1
        d.append (counter * str(counter))
        
    return "\n".join(d)
