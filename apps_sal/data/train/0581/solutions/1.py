n = [""]
for x in range(0,int(input())):
 k,l,e = list(map(int,input().split()))
 sum=0

 n = list(map(int,input().split()))

 for i in range(0,k):
  sum += n[i]
 sum += e

 if l%sum == 0:
   print("YES")
 else:
  print("NO")
