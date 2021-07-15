def countevenone(left,right,span,maxbincount):
    if span == 1:
        return bin(left).count('1')
    if span == 2:
        return bin(right).count('1')+bin(left).count('1')
    if span % 2 != 0:
        if left % 2 == 0:
            adds = span//2 + bin(right).count('1')
            left = left//2
            right = (right-1)//2
        else:
            adds = span//2 + bin(left).count('1')
            left = (left+1)//2
            right = right//2
        span = span//2
        maxbincount = maxbincount-1     
        countones = countevenone(left,right,span,maxbincount)*2 + adds 
    else:
        if left % 2 == 0:
            left = left//2
            right = right//2
            adds = span//2
            span = span//2
        else:
            adds = (span-2)//2 + bin(right).count('1') + bin(left).count('1')
            left = (left+1)//2
            right = (right-1)//2
            span = (span-2)//2
        maxbincount = maxbincount-1 
        countones = countevenone(left,right,span,maxbincount) * 2 + adds
    return countones
def countOnes(left, right):
    # Your code here!
    span = right-left+1
    maxbincount=len(bin(right).replace("0b",''))
    return countevenone(left,right,span,maxbincount)
