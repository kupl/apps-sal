def distinct(seq):
    mylist = []
    for i in seq:
        if i not in mylist:
            mylist.append(i)
    return mylist
