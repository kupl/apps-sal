def thue_morse(n):
    out = "0"
    while len(out) < n:
        out += out.replace('1', '2').replace('0', '1').replace('2', '0')
    
    return out[:n]
