def true_binary(n):
    temp=bin(n)[2:]
    res=[]
    for i in temp[-1]+temp[:-1]:
        res.append(1) if i=="1" else res.append(-1)
    return res
