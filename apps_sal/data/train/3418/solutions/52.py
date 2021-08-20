def reverse_list(l):
    length = len(l)
    reversed_list = []
    index = -1
    print('len = ', length)
    print('reversed_list = ', reversed_list)
    for i in l:
        print(l[index])
        reversed_list.append(l[index])
        index -= 1
    return reversed_list
