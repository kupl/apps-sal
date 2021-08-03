def find_slope(s):
    try:
        d = (s[3] - s[1]) // (s[2] - s[0])
        return str(d)
    except:
        return 'undefined'
