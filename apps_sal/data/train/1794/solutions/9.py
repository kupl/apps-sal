primes=[2,3,5,7,11,13,17,19,23,29,31]
for i in range(37,500,2):
    if all(i%j for j in primes): primes.append(i)

def statement1(s): return s%2 and s-2 not in primes

def statement2(p):
    possible_pairs=set()
    for i in range(2,int(p**.5)+2):
        if p%i==0:
            possible_pairs.add((i,p//i))
    good_pairs=[statement1(i+j) for i,j in possible_pairs]
    return sum(good_pairs)==1

def statement3(s):
    possible_pairs=set()
    for i in range(2,s//2+2):
        possible_pairs.add((i,s-i))
    good_pairs=[statement2(i*j) for i,j in possible_pairs]
    return sum(good_pairs)==1

def is_solution(a, b):
    return statement1(a+b) and statement2(a*b) and statement3(a+b)
