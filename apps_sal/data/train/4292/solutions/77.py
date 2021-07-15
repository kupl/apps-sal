def string_clean(s):
    ans=''
    s=list(s)
    digits=['1','2','3','4','5','6','7','8','9','0']
    for i in s:
        if i in digits:
            continue
        ans=ans+i
    return ans
