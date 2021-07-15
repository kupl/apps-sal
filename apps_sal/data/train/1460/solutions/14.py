(D,X,Y)=list(map(int,input().split()))
s=list(map(int,input().split()))
T=[]
for _ in range(6):
    T.append(Y)
    Y=Y-(Y/50)
t=0
for i in s:
    t=t+T[i-1]
p=D*X+t
if(p>=300):
    print("YES")
else:
    print("NO")
    
    


    
    

