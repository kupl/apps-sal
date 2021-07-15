for i in range(int(input())):
 a = int(input())
 l = []
 for num in range(2,a + 1):  
  if num > 1:  
   for i in range(2,int(num**.5)+1):  
    if (num % i) == 0:  
     break 
   else:  
    l.append(num)
 print(sum(l))
