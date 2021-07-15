import math
def primeFactors(n):
    ar=[]
    while n%2==0: 
        ar.append(2) 
        n=n/2 
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0: 
            ar.append(i) 
            n=n/i
    if n>2: 
        ar.append(n)
    ax='**'
    x=''
    for i in sorted(set(ar)):
        c=ar.count(i)
        if c>1:
            x+='('+str(i)+ax+str(c)+')'
        else: x+='('+str(int(i))+')'
    return x
