t= int(input())
for i in range(t):
 n = int(input())
 a1 = list(map(int,input().split()))
 b1 = list(map(int,input().split()))
 sum1 = 0
 sum2 = 0
 answer = 0
 for j in range(n) :
  if (sum1 == sum2) and (a1[j]==b1[j]):
   answer+=a1[j]
  sum1 = sum1+a1[j]
  sum2 = sum2+b1[j]
  
 print(answer)
