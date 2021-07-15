def number(lines):
    lis = []
    x = 1
    for i in lines:
        lis.append(str(str(x) + ": " + i))
        x += 1
    return(lis)
