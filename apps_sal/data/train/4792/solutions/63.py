def parse_float(string):
    for e in string:
        c=ord(e)
        if c==46 or (c>47 and c<58):pass
        else:return None
    return float(string)
