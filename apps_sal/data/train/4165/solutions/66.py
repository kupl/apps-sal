def uni_total(string):
    finalist = list()
    mylist = list(string)
    for x in mylist:
        finalist.append(ord(x))
    return sum(finalist)
