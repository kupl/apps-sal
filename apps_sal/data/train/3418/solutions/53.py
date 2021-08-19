def reverse_list(l):
    tab = []
    for x in range(len(l)):
        tab.append(l[-x - 1])
    return tab
