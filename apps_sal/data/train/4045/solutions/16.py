def number(lines):
    formatted=[]
    for x in range(len(lines)):
        formatted.append(str(x+1)+": "+lines[x])
    return formatted
