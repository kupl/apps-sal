# cook your dish here
t = int(input())

for i in range(t):
 a,b = list(map(int,input().split()))
 
 #x=min(a,b)
 #y=max(a,b)
 count=0

 # for i in range(1,a+1):
 #     for j in range(1,b+1):
   
 #         if (i+j) %2 ==0:
 #             count+=1
 
 #x = list(range(1,a+1))
 #y = list(range(1,b+1))
 
 #print(a,b)
 
 if a % 2 != 0:
  even_x = a//2
  odd_x = a//2 +1
 else:
  even_x = a//2
  odd_x = a//2
  
 if b % 2 !=0:
  even_y = b//2
  odd_y = b//2 +1
 else:
  even_y = b//2
  odd_y = b//2
  
 #print("even_x & even_y : ",even_x,even_y)
 #print("odd_x & odd_y : ",odd_x,odd_y)
 count = (even_x * even_y) + (odd_x * odd_y)
 
 
 print(count)
 #print()

