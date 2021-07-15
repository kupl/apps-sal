def solution(digits):
    l=len(digits)
    start,end,max=0,5,0
    while 1:
        a=(digits)[start:end]
        if int(a)>max:
            max=int(a)
        start+=1
        end+=1
        if end==l+1:
            break
    return max
