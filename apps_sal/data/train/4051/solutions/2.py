def toUnderScore(name):
    if len(name) ==0:
        return ""
    hold=[]
    for x in name:
        hold.append(x)
    for index, elem in enumerate(hold):
        if index !=0:
            test = hold[index-1]
            if elem.isupper() and test != "_":
                hold.insert(index, "_")
            if elem.isdigit() and test.isalpha():
                hold.insert(index, "_")
                
    output= ''.join(hold)
    return output
    pass
