def solution(a, b):
    res = ''
    if len(a)>len(b):
        res = b+a+b
    else:
        res = a+b+a
    return res
        
    
    #if a!=b:
        #return min(a,b)+ max(a,b)+ min(a,b)

