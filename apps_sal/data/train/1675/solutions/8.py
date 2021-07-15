
t=int(input())
for _ in range(t):
    empty=input()
    n=int(input())
    
    list1=[]
    for _ in range(n):
        x,y=list(map(int,input().strip().split()))
        list1.append([x,-y])
    
    list1.sort()
   
    net=0
    for i in range(n-1):
        x1=list1[i][0]
        y1=-list1[i][1]
        x2=list1[i+1][0]
        y2=-list1[i+1][1]
        
        distance=((x2-x1)**2+(y2-y1)**2)**(0.5)
        net+=distance
    
    print(format(net,'.2f'))

