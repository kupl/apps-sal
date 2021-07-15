from collections import defaultdict
import operator

for i in range(int(input())):
    s=input()
    s=s.replace('b','1')
    s=s.replace('w','0')
    compare=int(s,2)

    n=int(input())
    List=[]
    for i in range(n):
        bin=input()
        bin=bin.replace('+','1')
        bin=bin.replace('-','0')
        num=int(bin,2)
        List.append(num)
    
    length=int(2**n)
    count=int(0)
    i=j=int(0)
    for i in range(length):
         x=0;
         for j in range(0,n):
                 if i&(1<<j)>0:
                        x=operator.xor(x,List[j])
         
         if(operator.xor(x,compare)==1023):
                count+=1
         
    print(count)
  
       
    
            
                
            
    
    
    
    
