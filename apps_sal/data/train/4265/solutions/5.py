def tops(msg):
    res=''
    top=1
    diff=5
    while top<len(msg):
        res+=msg[top]
        top+=diff
        diff+=4
    return res[::-1]
