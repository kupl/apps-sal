t=int(input())
for _ in range(t):
 n=input()
 l1=[]
 for i in n:
  if i not in l1:
   l1.append(i)
 print(len(l1))
