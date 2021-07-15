def to_alternating_case(string):
    x=[]
    for i in list(string):
        if i.isupper():
            x.append(i.lower())
        elif i.isspace():
            x.append(" ")
        else:
            x.append(i.upper())
    return "".join(x)

