def solve(a, b):
    alis = 0
    bob = 0
    for i in range(3):
        if(a[i]>b[i]):
            alis+=1
        elif(a[i]<b[i]):
            bob+=1
    if(alis==bob):
        return str(bob)+", "+str(alis)+":"+' that looks like a "draw"! Rock on!'
    elif(max(alis,bob)==alis):
        return str(alis)+", "+str(bob)+":"+' Alice made "Kurt" proud!'
    else:
        return str(alis)+", "+str(bob)+":"+' Bob made "Jeff" proud!'

