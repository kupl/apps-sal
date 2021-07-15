import itertools

def statement1(s):
    return s%2 and not(is_prime(s-2))

def statement2(p):
    
    return len(get_posses(p)) == 1



def statement3(s):
    posses = ( [a,s-a] for a in range(s))
    posses = {tuple(sorted(i) ) for i in posses if min(i) >=2}
    
    finals = [ [a,b] for [a,b] in posses if statement2(a*b)]
    return len(finals) == 1

def is_solution(a, b):
    return statement1(a+b) and statement2(a*b) and statement3(a+b)
    
def get_posses(p):
    posses = [ (a,b)
    for a,b in ineff_poss_factors(p)
        if statement1(a+b)
        ]
    return posses
    
def is_prime(n):
    return len(list(prime_factors(n))) == 1
    
def ineff_poss_factors(n):
    for i in itertools.count(start = 2):
        if i**2 > n: break
        
        if not (n%i):
            yield (i, n//i)
    
def prime_factors(n):
    
    for i in itertools.count(start = 2):
        if i**2 > n: break
        if not n% i:
            yield i
            n//= i
    if n > 1:
        yield n
