for _ in range(int(input())):
    n=int(input())
    
    if n%7==0:
        print(n)
    elif n<17 and n==1 or n==2 or n==3 or n==5 or n==6 or n==9 or n==10 or n==13 or n==17:
        print(-1)
    else:
        found=False
        while not found:
            n-=4
            if n%7==0:
                print(n)
                found=True
            elif n%4==0:
                temp=n
                while temp>0:
                    temp-=4
                    if temp%7==0:
                        break
                    
                if temp>0 and temp%7==0:
                    print(temp)
                else:
                    print(0)
                    
                found=True
        
