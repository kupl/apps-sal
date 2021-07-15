def hex_to_dec(s):
    key = "0123456789abcdef"
    n=0
    res=0
    for l in s[::-1]:
        res += key.index(l)*(16.**n)
        n+=1
        
    return int(res)
