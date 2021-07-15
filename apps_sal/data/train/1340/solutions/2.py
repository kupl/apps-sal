for _ in range (int(input())):
 n = int(input())
 a = [int(i) for i in input().split()]
 tp = 0
 s = 0
 for i in range (n):
  if a[i]>0:
   tp+=1
   s+=a[i]
 ans=[]
 for i in range(tp):
  if a[i]<=0:
   ans.append(i+1)
 for i in range (tp,n):
  if a[i]>0:
   ans.append(i+1)
 print(s)
 print(len(ans),*ans)
