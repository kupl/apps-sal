def reverse_middle(lst):
    return lst[(len(lst)//2)-1:(len(lst)//2)+1+(1 if len(lst)%2!=0 else 0)][::-1]

