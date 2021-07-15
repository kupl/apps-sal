for _ in range(int(input())):
 a,b,c=map(int,input().split(':'))

 if b in[1,3,5,7,8,10,12]:
  print(int((31-c)/2+1))
  continue
 if b in [4,6,9,11]:
  print(int((61-c)/2+1))
  continue
 if a%400==0 or a%100!=0 and a%4==0:
  print(int((29-c)/2+1))
  continue
 else:
  print(int((59-c)/2+1))
  continue
