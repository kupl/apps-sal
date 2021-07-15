def capitalize(s,ind):
    temp = list(s)
    for i in ind:
        if i > len(temp):
            return "".join(temp)
        temp[i] = temp[i].upper()
    return "".join(temp)
