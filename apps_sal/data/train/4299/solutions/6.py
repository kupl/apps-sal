
import math
def is_prime_happy(n):
    print(n)
    if n==0 or n ==2 or n ==1:
        return False
#     if n ==2:
#         return True

     
    a=[2]
    for num in range(3,n,2):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
#             print(num)
            a.append(num)
    print(a)
    print(sum(a))
    if sum(a)==n  :
        
        return True
    if sum(a)%n==0 :
        return True
    
    return False    
