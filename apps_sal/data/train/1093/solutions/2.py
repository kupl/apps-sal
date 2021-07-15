from sys import stdin

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def getPrime(n):
    
    arr = [0]*25
    for i,p in enumerate( primes ):
        if p > n:
            break
        
        while n % p == 0:
            arr[i] += 1
            n //= p
            
    
    return arr


def matAdd(matA , matB):
    
    arr = []
    for i in range(25):
        arr.append( matB[i] + matA[i] )
        
    return arr


def matSub( matA , matB ):
    
    arr = []
    
    for i in range(25):
        arr.append( matA[i] - matB[i] )
        
    return arr


def getPow( arr , M ):
    
    ans = 1
    
    for i , a in enumerate( arr ):
        
        if a != 0:

            ans *= pow( primes[i] , a , M )
        
            if ans > M:
                ans %= M
            
    return ans%M



n = int(input())
arr = list(map(int,input().strip().split()))

temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pref = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]


for a in arr:
    
    for i,p in enumerate( primes ):
        if p > a:
            break
        
        while a % p == 0:
            temp[i] += 1
            a //= p
    
    pref.append( temp.copy() )

    
for po in range( int(input()) ):
    
    a , b , M = map( int , input().strip().split() )
    
    ans = getPow( [ x-y for (x,y) in zip( pref[b] , pref[a-1] ) ] , M )
        
    print(ans%M)
