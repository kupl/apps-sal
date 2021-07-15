def flatten(*arr):
    inputlist = list(arr)
    while (True):
        typelist =[]
        for i in inputlist:
            typelist.append(type(i))
        if list in typelist:
            inputlist = takeoff(inputlist)
        else:
            return inputlist
def takeoff(inputlist):
    output =[]
    for i in inputlist:
        if type(i)==list:
            output.extend(i)
        else:
            output.append(i)
    return output
