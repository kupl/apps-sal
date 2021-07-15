t=int(input())
i=0
while i<t:
    i=i+1
    n=int(input())
    sum=0
    
    while n>0:
        if n%10==4:
            sum=sum+1
            n=n//10
        
        else:
            n=n//10
    print(sum) 

