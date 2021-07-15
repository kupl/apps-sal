def count(a, t, x):
    result=0
    for n in a:
        if n==t or (x!=0 and (n-t)%x==0):
            result+=1
    return result
