def reverse_list(l):
    li = []
    for n in range(0, len(l)):
        li.append(l[len(l) - n - 1])
    return(li)
