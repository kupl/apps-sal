def parse_float(string):
    for i in ''.join(string): 
        if i in 'abcdefghijklmnopqrstuvwxyz': return None
    return float(''.join(string))
