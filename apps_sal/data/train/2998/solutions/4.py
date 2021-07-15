def atomic_number(electrons):
    result=[]
    shield=1
    maxnum=2
    if electrons==1:
        return [1]
    while electrons>maxnum:
        result.append(maxnum)
        electrons-=maxnum
        shield+=1
        maxnum = shield ** 2 * 2
    result.append(electrons)
    return result

