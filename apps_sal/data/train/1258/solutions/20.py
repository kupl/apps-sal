# cook your dish here
t=int(input())
for loop in range(t):
 n=input()
 sum=0
 addable=0
 for i in n:
  sum+=ord(i)-ord('0')
  addable+=ord('9')-ord(i)
 rem=sum%9
 if(int(n)>9):
  
  if(rem>9-rem):
   if(9-rem<=addable):
    print(9-rem)
   else:
    print(rem)
  else:
   if(sum>rem):
    print(rem)
   else:
    print(9-rem)
 else:
  print(min(rem,9-rem))
