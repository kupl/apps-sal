import math
def primes(x,y):
    a=''
    for num in range(x,y,2):
        if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
            a=a+str(num)
    return a
def solve(a, b):
    print((a, b))
    return primes(1,50000)[a:a+b]
    
    

