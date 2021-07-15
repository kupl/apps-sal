# cook your dish here
def read_i_l(l=False):
    m = list(map(int, input().strip().split(" ")))
    if l:
        return list(m)
    else:
        return m
def i():
    return int(input().strip())
import math
# A function to print all prime factors of  
# a given number n 
def nbOddEvenprimeFactors(n): 
    nb_odd=0
    nb_even=0
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        n = n / 2
        nb_even+=1
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            nb_odd+=1
            n = n / i 
    if n > 2:
        nb_odd+=1
    
    return nb_even, nb_odd              
 
T = i()
for _ in range(T):
    N = i()
    if N == 1:
        print("Grinch")
    elif N == 2:
        print("Me")
    elif N % 2 == 1:
        print("Me")
    else:
        #print(N, nbOddprimeFactors(N))
        e, o = nbOddEvenprimeFactors(N)
        if o == 0 or (e == 1 and o == 1):
            print("Grinch")
        else:
            print("Me")
