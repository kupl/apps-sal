# cook your dish here
for j in range(int(input())):
 n=input()
 c=sum(map(int,n))
 if(len(n)>1 and c<9):
  print(9-c)
 else:
  print(min(c%9,9-c%9))
