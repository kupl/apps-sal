def reverse_by_center(s):
    l=len(s)//2
    return s[l:]+s[:l] if l*2==len(s) else s[l+1:] +s[l]+s[:l]
