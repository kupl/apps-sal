def parse_float(string):    
    return float(''.join(string)) if ''.join(''.join(string).split('.')).isdigit() else None
