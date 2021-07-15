# cook your dish here

# def getSum(n): 
#     sum = 0
#     while (n != 0): 
#         sum = sum + int(n % 10) 
#         n = int(n/10) 
#     return sum
 

for _ in range(int(input())):
 n = input()
 s=0
 for i in n:
  s+=int(i)
 if s<9 and len(n)!=1:
  print(9-s%9)
 else:
  print(min(9-s%9,s%9))
