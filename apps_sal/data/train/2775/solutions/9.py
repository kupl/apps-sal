def likes(names):
    l = len(names)
    s = 'no one likes this'
    if l == 1:
        s = names[0] + ' likes this'
    elif l == 2:
        s = ' and '.join(names) + ' like this'
    elif l == 3:
        s = ', '.join(names[:-1]) + ' and ' + names[-1] + ' like this'
    elif l != 0:
        s = ', '.join(names[:2]) + ' and ' + str(l - 2) + ' others like this'
    return s
