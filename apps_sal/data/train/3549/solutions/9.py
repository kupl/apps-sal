def reverse_middle(lst):
    return lst[::-1][len(lst)//2-1:len(lst)-len(lst)//2+1]
