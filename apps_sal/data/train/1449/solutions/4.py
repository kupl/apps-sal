#import psyco
#psyco.full()

for _ in range(int(input())):
    s=input().strip()
    ways=0
    l=len(s)
    
    index=[]
    for i in range(l):
        if s[i]=='4':
            index.append(i)
    ways=0        
    for i in range(len(index)):
        if i==0:
            ways+=(index[i]+1-0)*(l-index[i])
        else:
            ways+=(index[i]-index[i-1])*(l-index[i])
            
    print(ways)
