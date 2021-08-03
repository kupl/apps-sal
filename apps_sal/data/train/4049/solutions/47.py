def monkey_count(n):
    mylist = []
    num = int(n)
    num += 1
    for el in range(num):
        mylist.append(el)
    return mylist[1::]
