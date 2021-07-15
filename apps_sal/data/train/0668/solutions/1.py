# cook your dish here
t=int(input())
for i in range(t):
    
    l=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    if (sum(l2)>0):
        x=0
        if l[1]==1:
            h=l2
            y=0
            
            for j in range(len(h)):
                y=max(0,y+h[j])
                x=max(y,x)
            print(x)
        else:  
            h=l2+l2
            y=0
            
            for j in range(len(h)):
                y=max(0,y+h[j])
                x=max(y,x)
            print(x+(l[1]-2)*sum(l2))
            
        
        
    else:
        if max(l2)<0:
            print(max(l2))
        else:
            x=0
            if l[1]==1:
                h=l2
                y=0
                
                for j in range(len(h)):
                    y=max(0,y+h[j])
                    x=max(y,x)
                print(x)
            else:  
                h=l2+l2
                y=0
                
                for j in range(len(h)):
                    y=max(0,y+h[j])
                    x=max(y,x)
                print(x)
            
            
            

