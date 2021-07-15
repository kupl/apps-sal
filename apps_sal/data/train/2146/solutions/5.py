import sys
input = sys.stdin.readline

n,d,m=list(map(int,input().split()))
A=list(map(int,input().split()))

P=[]
M=[]

for a in A:
    if a>m:
        P.append(a)
    else:
        M.append(a)

P.sort(reverse=True)
M.sort(reverse=True)

if P==[]:
    print(sum(M))
    return

ANS=sum(M)+P[0]

useP=1
useM=len(M)
SUM=ANS

#print(ANS)

while 0<=useP<=len(P) and 0<=useM<=len(M):
    if n-(useP+useM+1)>=useP*d:
        useP+=1

        if useP>len(P):
            break
        
        SUM+=P[useP-1]

    else:
        if useM==0:
            break
        
        SUM-=M[useM-1]
        useM-=1

    #print(useP,useM,SUM)

    ANS=max(ANS,SUM)

print(ANS)
    
    
    


