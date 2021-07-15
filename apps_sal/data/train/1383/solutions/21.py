import math 
def no_of_factors(n) : 
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1) : 
        if (n % i == 0) : 
            if (n / i == i) : 
                count = count + 1
            else :
                count = count + 2

    return count 

t = int(input())
for i in range(t):
    n,k1,k2 = [int(x) for x in input().split()]
    p1,p2,p3,p4 = [int(x) for x in input().split()]
    l = [-1 for x in range(k2-k1+1)]
    for x in range(k1,k2+1):
        fact = no_of_factors(x)
        cont = x-k1
        if fact == 3:
            l[cont] = p1
        elif fact%2==1:
            l[cont] = p2
        else:
            l[cont] = p3
    total = 0
    for x in l:
        total+=x
    print(total)
