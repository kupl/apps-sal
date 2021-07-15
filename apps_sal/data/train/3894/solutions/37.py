def solve(s):
    lcase,ucase=0,0
    for i in s:
        if i.isupper():
            ucase=ucase+1
        else:
            lcase=lcase+1
    return s.lower() if lcase>=ucase else s.upper()

