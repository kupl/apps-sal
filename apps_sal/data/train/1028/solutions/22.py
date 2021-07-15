# cook your dish here
for _ in range(int(input())):
    num = int(input())
    num_original =num2=num
    sum1 = 0
    cnt=0
    
    while(num>0):
    	cnt=cnt+1
    	num=num//10
    
    while num2>0:
       rem = num2% 10
       sum1 += rem ** cnt
       num2//= 10
    
    
    if(num_original==sum1):
        print("FEELS GOOD")
    else:
        print("FEELS BAD")
            
        
    
    

