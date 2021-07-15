def reverse_by_center(s):
    l = len(s)
    return  s[l//2+1:]+s[l//2]+s[:l//2] if l%2 else s[l//2:]+s[:l//2]
