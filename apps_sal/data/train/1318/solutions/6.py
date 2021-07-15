case=int(input())
for c in range(case):
 l,k=map(int,input().split())
 sum=0
 for i in range(1,(l-k)+2):
  sum+=i
 print("Case {}:".format(c+1),sum)
