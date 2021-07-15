def problem(a):
    
        
    if type(a) == int:
        return (a * 50)+6
    if type(a) == float:
        return int(a * 50) + 6
    else: 
        return "Error"
