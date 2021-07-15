def find_needed_guards(k):
    
    prev = True
    guards = 0
    for i in k:
        if not i and not prev:
            guards += 1
            prev = True
        else:
            prev = i
            
    return guards
