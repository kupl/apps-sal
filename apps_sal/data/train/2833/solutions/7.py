def sect_sort(l, ind, n=-1):
    if(n > 0):

        s = sorted(l[ind:ind + n])
        return l[0:ind] + s + l[ind + n:]
    else:
        s = sorted(l[ind:])
        return l[0:ind] + s
