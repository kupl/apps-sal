tc=int(input())
for i in range(tc):
 length=int(input())
 l1=input().split()
 l1 = list(set(l1))
 new_length=len(l1)
 diff=length-new_length
 if diff%2==1:
  diff=diff+1
 print(length-diff)
