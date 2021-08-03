def merge_arrays(first, second):
    newlist = []
    for eachvalue in first:
        if eachvalue not in newlist:
            newlist.append(eachvalue)
    for eachvalue in second:
        if eachvalue not in newlist:
            newlist.append(eachvalue)
    return sorted(newlist)
