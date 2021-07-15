def cumul(n) :
    return n*(n+1)//2

# length of the line for the n index
def length (n) :
    res = cumul(n)
    length = len(str(n))
    i = 1
    while length>1 :
        res += cumul (n-(10**i -1))
        length -=1
        i+=1
    return res 


def calculindex(d) : 
    if d <= 9 :
        return d
    
    index = index_old = 9     
    i=0
    while d> index :
        index_old = index 
        i+=1
        index = index_old +  9*(i+1)*10**i        
    d-= index_old
    if d%(i+1)== 0 :
        return (str(10**(i)+d//(i+1) -1)[-1])
    else :
        return (str(10**(i)+d//(i+1))[d%(i+1)-1])
    

def solve(n):
    print(n)
    if n<=2:
        return 1
    min = 1
    max = n
    val = int(n//2)+1
    
    while length(min)< n< length(max) and max-min>1 :
        if length(val)>n :
            max,val = val,(val+min)//2
        elif length(val)< n:
            min,val = val,(max+val)//2     
        else :
            return int(str(val)[-1])    
    dist = n-length(min)
    
    return int(calculindex(dist))
