def reverse_middle(lst):
    l = len(lst)//2 - 1
    return lst[l:-l][::-1]
