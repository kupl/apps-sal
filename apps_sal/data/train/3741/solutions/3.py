def vector_affinity( a, b ):
    sizeA = len(a)
    sizeB = len(b)

    if (sizeA + sizeB) == 0:
        return 1.0

    if sizeA >= sizeB:
        den = sizeA
        numIter = sizeB
    else:
        den =  sizeB
        numIter = sizeA

    numMatch=0

    for i in range(numIter):
        if a[i]==b[i]:
            numMatch+=1

    affinity = numMatch/den

    return affinity
#----end function

