def solve(a, b):
    alic = 0
    bob = 0
    for i in range(3):
        if(a[i] > b[i]):
            alic+=1
        elif(a[i]<b[i]):
            bob+=1
    if (alic == bob):
        return str(bob)+", "+str(alic)+":"+' that looks like a "draw"! Rock on!'
    elif (max(alic,bob) == alic):
        return str(alic)+", "+str(bob)+":"+' Alice made "Kurt" proud!'
    else:
        return str(alic)+", "+str(bob)+":"+' Bob made "Jeff" proud!'

