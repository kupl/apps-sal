test_case = int(input())
for i in range(0,test_case):
 line = input().split(' ')
 N = int (line[0])
 K = int (line[1])
 ans = []
 for i in range(1,N+1):
  if i%2==0:
   ans.append(0-i)
  else:
   ans.append(i)
 
 temp = K - int((N+1)/2)
 ind = N-1
 if temp>0:
  while temp>0:
   if ans[ind]<0:
    ans[ind] = 0-ans[ind]
    temp = temp - 1 
   ind = ind - 1
 else:
  temp = 0 - temp
  while temp>0:
   if ans[ind]>0:
    ans[ind] = 0-ans[ind]
    temp = temp -1
   ind = ind - 1
 for i in range(0,N):
  print(ans[i], end=" ")
 print()
