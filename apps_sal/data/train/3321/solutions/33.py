def evil(n):
    _odious = "It's Odious!"
    _evil = "It's Evil!"
    
    is_evil = True
    for degree in evilometer(n):
        is_evil = not is_evil
    
    return is_evil and _evil or _odious
        
def evilometer(n):
    while n != 0:
        if n % 2 == 1:
            yield
        n = n // 2
    
def expand_to_string(n):
    binary = ""
    while n != 0:
        binary += str(n % 2)
        n = n // 2
    return binary
