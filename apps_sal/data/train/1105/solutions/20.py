# cook your dish here
# cook your dish here
for i in range(int(input())):
 N=int(input())
 C=list(map(int,input().split()))
 C.sort(reverse=True)
 b1=b2=0
 for i in range(N):
  if b1<b2:
   b1+=C[i]
  else:
   b2+=C[i]
 print(max(b1,b2))
