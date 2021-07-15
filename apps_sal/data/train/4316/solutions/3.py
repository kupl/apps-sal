def reverse_by_center(s):
    m = len(s)//2
    
    return s[m:] + s[:m] if len(s) % 2 == 0 else s[m+1:] + s[m] + s[:m]
