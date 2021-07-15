# cook your dish here
# cook your dish here
n=int(input())
l=[]
for j in range(n):
    t=int(input())
    l.append(t)
    


def pat(n):
    c=1
    for i in range(0,n,1):
        for j in range(0,n,1):
            print(c,end='')
            c+=1
        print()
        
    
for i in range(n):
    pat(l[i])
    
    
    
    
