def check(seq, elem):
    grade=0
    for i in seq:
        if i==elem:
            grade+=1
    if grade>0:
        return(True)
    else:
        return(False)

