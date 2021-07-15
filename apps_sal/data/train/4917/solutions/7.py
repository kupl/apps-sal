def validBraces(s):
    pairs = ['{}', '()', '[]']
    while any(pair in s for pair in pairs):
        for pair in pairs: 
            s = s.replace(pair, "")
    return s == ""
