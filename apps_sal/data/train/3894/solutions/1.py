def solve(s):
    upper = 0
    lower = 0
    
    for char in s:
        if char.islower():
            lower += 1
        else:
            upper += 1
            
    if upper == lower or lower > upper:
        return s.lower()
    else:
        return s.upper()
