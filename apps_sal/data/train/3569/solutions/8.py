def is_lucky(ticket):
    if len(ticket) != 6:
        return False
    
    total = 0
    
    for i, c in enumerate(ticket):
        if not c.isdigit():
            return False
            
        if i < 3:
            total += int(c)
        else:
            total -= int(c)
    
    return total == 0
