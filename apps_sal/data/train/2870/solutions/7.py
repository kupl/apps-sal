def same(arr_a, arr_b):
    if len(arr_b)!=len(arr_a): return False
    temp1=temp2=[]
    for i,j in zip(arr_a, arr_b):
        temp1.append(sorted(i))
        temp2.append(sorted(j))
    while temp1 and temp2:
        try:
            temp2.remove(temp1.pop())
        except:
            return False
    return True
