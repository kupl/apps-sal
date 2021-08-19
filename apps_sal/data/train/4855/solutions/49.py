def vert_mirror(string):
    mylist = string.split('\n')  # splits into list of the parts
    for x in range(len(mylist)):
        mylist[x] = mylist[x][::-1]
    mystring = '\n'.join(mylist)
    return mystring


def hor_mirror(string):
    mylist = string.split('\n')
    mylist = mylist[::-1]
    mystring = '\n'.join(mylist)
    return mystring


def oper(fct, s):
    if fct == vert_mirror:
        return vert_mirror(s)
    elif fct == hor_mirror:
        return hor_mirror(s)
