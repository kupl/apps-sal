for _ in range (int(input())):
 n1=int(input())
 sum1=0
 for i in range(n1):
  li=[int(i) for i in input().split()]
  li.pop(0)
  if len(li)%2==0:
   n=(len(li))//2
  else:
   n=(len(li)//2)+1
  sum1+=sum(li[:n])
 print(sum1)
 
  

