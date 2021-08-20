def digitize(n):
    mylist = []
    a = list(str(n))
    for i in a:
        mylist.append(int(i))
    mylist.reverse()
    return mylist
