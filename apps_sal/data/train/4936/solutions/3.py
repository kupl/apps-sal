def reverse(lst):
    empty_list = list()
    for i in range(len(lst)):
        empty_list.append(lst.pop())
    return empty_list
