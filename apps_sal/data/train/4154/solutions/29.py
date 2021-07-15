def is_triangle(a, b, c):
    llist = [a,b,c]
    llist.sort()
    highest = llist[2]
    sumrest = llist[0] + llist[1]
    if highest < sumrest:
        return True
    return False
