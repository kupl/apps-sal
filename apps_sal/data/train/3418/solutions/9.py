def reverse_list(l):
    new_list = []
    for i in l:
        new_list = [i] + new_list
    return new_list
