def hex_to_dec(s):
    
    key = '0123456789abcdef'
    
    return sum([key.index(v)*16**(len(list(s))-1-i)for i, v in enumerate(list(s))])

