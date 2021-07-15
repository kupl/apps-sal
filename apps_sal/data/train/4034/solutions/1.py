def sillycase(s):
    l = len(s)
    return s[:l//2+l%2].lower() + s[l//2+l%2:].upper()
