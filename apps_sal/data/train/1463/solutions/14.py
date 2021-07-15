import math
for _ in range(int(input())):
    x=int(input())
    if x==1:
        print("1")
        print("1"+' 1')
    elif x==2:
        print('1')
        print('2'+' 1'+' 2')
    elif x==3:
        print('1')
        print('3'+' 1'+' 2'+' 3')
    else:
        c=x//2
        if x%2==0:
            print(c)
            for i in range(1,x,2):
                print("2",end=' ')
                print(i,end=' ')
                print(i+1)
             
        else:
            print(c)
            print('3'+' 1'+' 2'+' 3')
            for i in range(4,x,2):
                print('2',end=' ')
                print(i,end=' ')
                print(i+1)
                
        
            
