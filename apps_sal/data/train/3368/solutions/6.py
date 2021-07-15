def circular_prime(n):
    #test is a number is a circular prime
    # uses 2 functions
   
    l=len(str(n)) # the length of the number  
    
    for i in range (l):
        
        if is_prime(n):  
            n=circul_num(n,l)
        else: # the num is not prime 
            return False # return False
    return True

def circul_num(n,l):
    # one  circular permutation of a num to left 
    # input n: int number , l: length of number
    power =10**(l-1)    # poer of 10 to cut the number at highst digit

    if len(str(n))<l:   #if num is short, need a 0 at the end to compensate
        N=n*10        
    else: 
        N=(n%power)*10+(n//power) # permutation to the left
    return N

def is_prime(n):
    # chek if a number is praime
    if n==1:
        return False 

    for i in range(2,int(n**0.5)+1): #runs from 2 to the sqrt of n
        if n%i==0: 
            return False 
        
    return True

