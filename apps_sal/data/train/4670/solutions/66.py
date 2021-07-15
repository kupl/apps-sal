def string_to_number(s):
    if s[0]=="-":
        mul=-1
        i=1
    else:
        mul=1
        i=0
    ans=0
    while i<len(s):
        x=s[i]
        x=ord(x)-ord('0')
        ans=(ans*10)+x
        i=i+1
    return ans*mul
