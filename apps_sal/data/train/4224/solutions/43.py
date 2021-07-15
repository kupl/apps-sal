def dont_give_me_five(start,end):
    startlist=list(range(start,end+1))
    newlist=[]
    for item in startlist:
        if '5' not in str(item):
            newlist.append(item)
    return len(newlist)   # amount of numbers
