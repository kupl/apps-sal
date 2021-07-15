import sys
t=int(input(""))
while t:
    l2=[]
    count=0
    l=str(input(""))
    for i in range(len(l)-1):
        x=l[i]+l[i+1]
        if x not in l2:
            l2.append(x)
            count+=1
    print(count)
    t-=1

        
    

