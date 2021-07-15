def invert(lst):
    inverse_lst=[]
    for i in lst:
        if i < 0:
            inverse_lst.append(abs(i))
        else:
            inverse_lst.append(-i)
            
    return inverse_lst
