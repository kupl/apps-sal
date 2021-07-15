# cook your dish here
for i in range(int(input())):
 m,n = map(int,input().split())
 c = 0
 for i in range(m,n+1):
  p = str(i)
  if(p[-1] == "2" or p[-1] == "3" or p[-1] == "9"):
   c = c+1
 print(c)
