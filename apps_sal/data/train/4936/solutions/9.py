def reverse(lst):
    empty_list = list()
    for i in lst:
        empty_list = [i] + empty_list
    return empty_list
