def compare(s1,s2):
    return strsum(s1) == strsum(s2)

def strsum(x):
    if not type(x) == str: return 0
    if(x.upper().isalpha()): return sum(ord(v) for v in x.upper())
    return 0
