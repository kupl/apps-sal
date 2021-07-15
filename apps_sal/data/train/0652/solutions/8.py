# cook your code here
n=int(input())
while n>0:
 s1=input()
 
 s2=input()
 if s1.lower()<s2.lower():
  print("first")
 elif s1.lower()>s2.lower():
  print("second")
 elif s1.lower()==s2.lower():
  print("equal")
 n-=1
