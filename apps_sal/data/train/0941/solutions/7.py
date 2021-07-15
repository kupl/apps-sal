# cook your dish here
t = int(input())

for i in range(t):
 a,b = list(map(int,input().split()))
 count=0
 
 x = list(range(1,a+1))
 y = list(range(1,b+1))
 
 if len(x) % 2 != 0:
  even_x = len(x)//2
  odd_x = len(x)//2 +1
 else:
  even_x = len(x)//2
  odd_x = len(x)//2
  
 if len(y) % 2 !=0:
  even_y = len(y)//2
  odd_y = len(y)//2 +1
 else:
  even_y = len(y)//2
  odd_y = len(y)//2
 #print("even_x & even_y : ",even_x,even_y)
 #print("odd_x & odd_y : ",odd_x,odd_y)
 count = (even_x * even_y) + (odd_x * odd_y)
 print(count)

