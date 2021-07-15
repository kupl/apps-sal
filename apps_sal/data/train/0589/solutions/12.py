T = int(input())
ans = []

for _ in range(T):
 P = input()

 N = len(P)
 days = 0
 jumping_length = 1
 i = 0
 while(i<N):
  if(P[i]=='.'):
   j = i
   while(j<N and P[j]=='.'):
    j += 1
   if(j-i+1 > jumping_length):
    jumping_length = j-i+1
    days += 1
   i = j
  else:
   i += 1
 ans.append(days)

for i in ans:
 print(i)
