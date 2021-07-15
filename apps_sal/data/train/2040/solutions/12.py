import sys
from math import sqrt

def main():
    n,h=list(map(int,sys.stdin.readline().split()))
    
    sn=sqrt(n)
    result=[]
    for i in range(n-1):
        result.append(sqrt(i+1)*h/sn)
    
    sys.stdout.write(' '.join(map(str,result))+'\n')
    
main()


