def reverse_list(l):
    i = len(l)-1
    n = []
    p = 0
    while p != len(l):
        n.insert(p,l[i])
        p += 1
        i -= 1
    return n
