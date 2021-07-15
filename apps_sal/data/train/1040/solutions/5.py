# cook your dish here
T = int(input())
for _ in range(T):
 N,Q = [int(b) for b in input().split()]
 S = input()
 b = [0,0]
 l = 0
 for i in range(len(S)-2):
  a = S[i:i+3]
  if(a[0]==a[1] or a[0]==a[2] or a[1]==a[2]):
   l+=1 
  b.append(l)
 # print(b)
 for i in range(Q):
  L,R = [int(b) for b in input().split()]
  if(R-L<2):
   print("NO")
   continue
  if(b[R-1]-b[L]>0):
   print("YES")
  else:
   print("NO")
