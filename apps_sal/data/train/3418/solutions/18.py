def reverse_list(l):
    #'return a list with the reverse order of l'
    re = []
    for i in range(0, len(l)):
        re.append(l.pop())
    return re
