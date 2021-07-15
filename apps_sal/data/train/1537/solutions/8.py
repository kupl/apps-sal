import math
def isPrime(nm):
    for i in range(2,int(math.sqrt(nm)+1)):
        if nm%i==0:
            return False
    return True
U=list()
num=2
for i in range(10000):
    while(not isPrime(num)):
        num+=1
    U.append(num)
    num+=1
#print(U)
S=list()
for i in range(1,len(U)):
    if isPrime(i+1):
        S.append(U[i])
#print(len(S))
t=int(input())
for i in range(t):
    sum=0
    n=int(input())
    for j in range(n):
        sum+=S[j]
    #sum=sum%1000000007
    print(sum)
