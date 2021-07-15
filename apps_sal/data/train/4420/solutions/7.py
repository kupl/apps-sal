def prime_factors(n):
    if n%2==0 and n>0:return [2]+prime_factors(n//2)
       
    for a in range(3,int(n**.5)+1,2):            
        if n%a==0:return sorted(prime_factors(n//a)+prime_factors(a))        
    return [n] if n>1 else []

def mult_primefactor_sum(a, b): # [a, b] range of numbers included a and b
    return [c for c in range(a,b+1) if len(prime_factors(c))>1 and c%sum(prime_factors(c))==0]
