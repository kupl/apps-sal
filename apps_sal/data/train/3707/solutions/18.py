def sorter(textbooks):
    listtemp = [(x.lower(),x) for x in textbooks]
    listtemp.sort()
    return [x[1] for x in listtemp]
