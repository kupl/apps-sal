import sys

def main():
    s=sys.stdin.readline().rstrip()
    t=sys.stdin.readline().rstrip()
    
    result=[]
    
    iisl=0
    iisr=len(s)//2+len(s)%2-1
    iitl=0
    iitr=len(s)//2-1
    
    aas=list(sorted(list(s)))
    aat=list(sorted(list(t),reverse=True))
    rl=0
    rr=len(s)-1
    result=['?']*len(s)
    
    for i in range(len(s)):
        if i%2==0:
            if aas[iisl]<aat[iitl]:
                result[rl]=aas[iisl]
                iisl+=1
                rl+=1
            else:
                result[rr]=aas[iisr]
                iisr-=1
                rr-=1
        else:
            if aat[iitl]>aas[iisl]:
                result[rl]=aat[iitl]
                iitl+=1
                rl+=1
            else:
                result[rr]=aat[iitr]
                iitr-=1
                rr-=1
    
    sys.stdout.write(''.join(result)+'\n')
    
main()


