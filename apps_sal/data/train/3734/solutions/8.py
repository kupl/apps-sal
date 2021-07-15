def roll(desc, verbose=False):   
    if not desc:
        return False
    desc="".join(desc.split())  
    temp=""
    for i in desc:
        if i in "+-":
            break
        temp+=i
    for i in temp:
        if i not in "1234657890d":
            return False
    remain=desc[len(temp):]
    for i in remain:
        if i not in "1234657890d+-":
            return False
    for i in range(len(remain)-1):
        if remain[i+1] in "+-" and remain[i] in "+-":
            return False
    remain=eval(remain) if remain else 0
    temp=temp.split("d")    
    temp[0]=1 if not temp[0] else int(temp[0])
    return { "dice": [1]*temp[0], "modifier": remain } if verbose else 1*temp[0]+remain
