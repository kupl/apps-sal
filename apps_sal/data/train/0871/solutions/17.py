# your code goes here
# cook your dish here
from collections import Counter
t=int(input())
for x in range(t):
    inp = list(map(int,input().split()))
    r=inp[0]
    c=inp[1]
    listo=[]
    listb=set()
    pair=0
    for i in range(r):
        
        string=input()
        for j in range(len(string)):
            if(string[j]=='U'):
                listo.append([i,j,1])
            elif(string[j]=='D'):
                listo.append([i,j,2])
            elif(string[j]=='L'):
                listo.append([i,j,3])
            elif(string[j]=='R'):
                listo.append([i,j,4])
            elif(string[j]=='#'):
                listb.add((i,j))
    
                
    for y in range(max(r,c)):
        nants=Counter()
        for i in range(len(listo)):
            if(listo[i][2]!=5):
                nants[tuple(listo[i][:-1])]+=1
        for key in nants:
            pair+=(nants[key]*(nants[key]-1))//2
        
        for ant in listo:
            if(ant[2]==1):
                 ant[0]-=1
            elif(ant[2]==2):
                ant[0]+=1
            elif(ant[2]==3):
                ant[1]-=1
            elif(ant[2]==4):
                ant[1]+=1
            if(tuple(ant[:-1])) in listb:
                ant[2]=5
            elif(ant[0]<0) or ant[0]>=r:
                ant[2]=5
            elif ant[1]<0 or ant[1]>=c:
                ant[2]=5
    print(pair)
            
            
             
    
        
                
        
    

