# cook your dish here
import sys

def get_factors(n:int):
    for i in range(2, n//2+1):
        if(n%i==0):
            yield i

N,M=sys.stdin.readline().strip().split(" ")[:2]

N,M=int(N),int(M)
if(N in (0,1)): print(0)
#elif(N==1): print(2%M)
else:
    res=2**N-2
    for el in get_factors(N):
        res-=2**el-2
    print(res%M)
    
        
