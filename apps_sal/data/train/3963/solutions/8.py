from functools import reduce
def amicable_numbers(n1,n2):
    s1=reduce(lambda x,y: x+(y if n1%y==0 else 0), range(1, n1),0)
    s2=reduce(lambda x,y: x+(y if n2%y==0 else 0), range(1, n1),0)
    return s1==n2 and s2==n1
