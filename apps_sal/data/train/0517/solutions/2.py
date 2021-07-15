powersof2 = {}
nonperiodics= {}


def pow2(x, m):
    powersof2[0] = 1%m
    powersof2[1] = 2%m
    for i in range(2, x+1):
        powersof2[i] = (powersof2[i-1]*2)%m


def nonperiodicsfill(x):
    for i in range(x):
        nonperiodics[i]=0


def listoffactors(x):
    lista=[]
    for i in range(1, 1 + x//2):
        if x%i == 0 :
            lista.append(i)
    return lista


def sieve(x):
    for i in range(2, x):
        if prime[i]:
            for q in range(i*2, x, i):
                prime[q] = False


def nonPeriodicStrings(s,m):
   # print("\nNPS"+ str(s) +" "+ str(m) + "\n")
    if s==1:
        return 2%m
    if s in nonperiodics:
        return nonperiodics[s]
    if prime[s]:
        nps = (powersof2[s] - 2) % m
        nonperiodics[s] = nps
        return nps
 #   print(s)
    li = listoffactors(s)
   # print(li)
    nps = powersof2[s]
    for i in li:
        nps -= nonPeriodicStrings(i, m)
    #    print(nonPeriodicStrings(i,m))
        nps %= m
    nonperiodics[s] = nps
    return nps


cc = input().split(' ')
a= int(cc[0])
m= int(cc[1])
#print(a)
#print(m)
prime = [True for i in range(a+1)]
#m = int(input())
pow2(a, m)
#print(powersof2)
sieve(a+1)
#print(prime)
if prime[a]:
    l = powersof2[a] - 2
    print(l)
else:
    print(nonPeriodicStrings(a, m))




