def solve(s):
    up=[]
    low=[]
    for i in s:
            if i.isupper():
                 up.append(i)
            else:
                 low.append(i)
    if len(low)>len(up):
           return s.lower()
    elif len(low)<len(up):
            return s.upper()
    else:
            return s.lower()

