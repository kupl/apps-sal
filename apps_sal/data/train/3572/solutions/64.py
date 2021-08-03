def invite_more_women(arr=0):
    lst1 = [i for i in arr if i < 0]
    lst2 = [i for i in arr if i > 0]
    return len(lst1) < len(lst2)
