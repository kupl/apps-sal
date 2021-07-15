
def hot(n,i):
    if n == 1:
        return i
    if n%2:
        return hot(3*n+1,i+1)
    else:
        return hot(n/2,i+1)
    
def hotpo(n):
    i=0
    return hot(n,i)

