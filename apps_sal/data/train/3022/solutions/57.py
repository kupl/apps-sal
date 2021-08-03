def two_highest(arg1):
    mylist = list(dict.fromkeys(arg1))
    mylist = sorted(mylist, reverse=True)
    return mylist[0:2]
