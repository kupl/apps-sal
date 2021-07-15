A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
e = A.lower()
def to_alternating_case(s):
    t = []
    for i in s:
        if i in A:
            t.append(i.lower())
        elif i in e:
            t.append(i.upper())
        else:
            t.append(i)
    return "".join(t)   

            

