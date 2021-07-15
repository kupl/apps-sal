def reverse_middle(lst):
    middle=int(len(lst)/2)
    
    if len(lst)%2>0:
        return list(reversed(lst[middle-1:middle+2]))
    else:
        return list(reversed(lst[middle-1:middle+1]))
