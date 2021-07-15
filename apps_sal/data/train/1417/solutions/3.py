# cook your dish here
from collections import Counter
import string
import math
import sys
def array_int():
    return [int(i) for i in sys.stdin.readline().split()]
def vary(arrber_of_variables):
    if arrber_of_variables==1:
        return int(sys.stdin.readline())
    if arrber_of_variables>=2:
        return list(map(int,sys.stdin.readline().split())) 
def makedict(var):
    return dict(Counter(var))
# i am noob wanted to be better and trying hard for that
def printDivisors(n): 
    divisors=[]  
    # Note that this loop runs till square root 
    i = 1
    while i <= math.sqrt(n): 
          
        if (n % i == 0) : 
              
            # If divisors are equal, print only one 
            if (n//i == i) : 
                divisors.append(i) 
            else : 
                # Otherwise print both 
                divisors.extend((i,n//i)) 
        i = i + 1
    return divisors

def countTotalBits(num):
     
     # convert number into it's binary and 
     # remove first two characters 0b.
     binary = bin(num)[2:]
     return(len(binary))
for _ in range(vary(1)):
    n=vary(1)
    num=array_int()
    nt=makedict(num)
    st=set((1,2,3,4,5,6,7,8))
    for i in nt:
        if i in st:
            st.remove(i)
    if len(st)!=0:
        print(0)
    else:
        mini=float('inf')
        for i in nt:
            if nt[i]<mini:
                mini=nt[i]
                
        print(mini)



        
    
        
    
        
    

	



                






    
    

    
    


    

    



    


    














        

    

            
    





        
        
   

