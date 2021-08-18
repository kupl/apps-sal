def reverse_list(l):
    'return a list with the reverse order of l'
    list = []
    for items in l:
        list.insert(0, items)
        print(list)
    return list
