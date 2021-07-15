# cook your dish here
for tc in range(int(input())):
 
 n = int(input())
 
 li1 = list(map(int,input().split(' ')))
 li2 = list(map(int,input().split(' ')))
 walk = 0
 sum1 = 0 
 sum2 = 0
 for i in range(n):
  if li1[i] == li2[i] and sum1 == sum2:
   walk += li1[i]
  sum1 += li1[i]
  sum2 += li2[i]
 print(walk)
