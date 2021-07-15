from math import sqrt
is_prime    = lambda x: all(x%y!=0 for y in range(2,int(sqrt(x))+1))
statement1  = lambda s: s%2>0 and not is_prime(s-2)
statement2  = lambda p: 1 == sum(p%i==0 and statement1(i + p//i) for i in range(2,int(sqrt(p))+1))
statement3  = lambda s: 1 == sum(statement2(i * (s-i)) for i in range(2,s//2+1))
is_solution = lambda a,b: statement1(a+b) and statement2(a*b) and statement3(a+b)

