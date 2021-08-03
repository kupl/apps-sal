def reverse_middle(lst):
    if len(lst) % 2 == 1:
        return lst[len(lst) // 2 - 1:len(lst) // 2 + 2][::-1]
    else:
        return lst[len(lst) // 2 - 1:len(lst) // 2 + 1][::-1]
