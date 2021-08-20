def reverse_middle(lst):
    l = len(lst)
    return lst[(l + 1) // 2:l // 2 - 2:-1]
