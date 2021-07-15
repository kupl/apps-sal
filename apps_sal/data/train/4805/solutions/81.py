def check(seq, elem):
    k=0
    for i in range(len(seq)):
        if seq[i]==elem:
            k+=1
    if k>0: 
        return True 
    else:
        return False

