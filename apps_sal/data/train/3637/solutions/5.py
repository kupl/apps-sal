import math as mt   
MAX=10000  
prime=[True for i in range(MAX+1)] 
def Sieve():      
    prime[1]=False
      
    for p in range(2,mt.ceil(mt.sqrt(MAX))):   
        if prime[p]: 
           
            for i in range(2*p,MAX+1,p): 
                prime[i]=False
Sieve()                  
def num_primorial(n):
    count,num=0,1     
    prod=1
    while count<n:
          
        if prime[num]: 
            prod*=num 
            count+=1
        num+=1
    return prod 
