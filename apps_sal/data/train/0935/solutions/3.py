# cook your dish here
T = int(input())
for i in range(T):
 X = int(input())
 if(X % 10 == 0):
  print(0)
 elif(X % 5 == 0):
  print(1)
 else:
  print(-1)

