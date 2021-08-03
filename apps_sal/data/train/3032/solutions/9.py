def factorsRange(n, m):
    dlist = {}
    for x in range(n, m + 1):
        templist = []
        for y in range(2, x + 1):
            if x % y == 0 and x != y:
                if templist.count(y) == 0:
                    templist.append(y)
        if len(templist) >= 1:
            dlist.update({x: templist})
        else:
            dlist.update({x: ["None"]})
    return dlist
