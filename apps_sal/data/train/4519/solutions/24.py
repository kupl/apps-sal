def max_number(n):
    
    l = []
    
    for pos, digit in enumerate(str(n)):
        l.append(digit)
    return int(''.join(sorted(l, reverse=True)))

