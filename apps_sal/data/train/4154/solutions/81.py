def is_triangle(a, b, c):
    mylist = [a, b, c]
    mylist.sort()
    if (mylist[0] + mylist[1]) > mylist[2]:
        return True
    else:
        return False
