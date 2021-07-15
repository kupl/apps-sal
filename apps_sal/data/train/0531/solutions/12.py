t = int(input())
listt = []
ans = 2

for x in range(t):
 a,b = map(int,input().split())
 listt.append([a,b])
 
i = 1

while i+1<t:
 if listt[i][0] - listt[i][1] > listt[i-1][0]:
  ans = ans+1
 elif listt[i][0] + listt[i][1] < listt[i+1][0]:
  ans = ans+1
  listt[i][0] = listt[i][0]+listt[i][1]
  
 i = i+1
if t == 1:
 print('1')
else:
 print(ans)
