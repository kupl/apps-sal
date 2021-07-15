def is_triangle(a, b, c):
    mylist = [a, b, c]
    mylist = sorted(mylist)
    if mylist[0] < mylist[1] + mylist[2] :
        if mylist[1] < mylist[0] + mylist[2]:
            if mylist[2] < mylist[0] + mylist[1]:
                return True
    return False

