def house_numbers_sum(inp):
    returnlist = []
    for eachnum in inp:
        if eachnum == 0:
            return sum(returnlist)
        else:
            returnlist.append(eachnum)
