def minTasks(diff, buttons):
 """Time Complexity : O(len(diff) + len(buttons))"""
 i,j=0,0
 incompleteTasks=0
 while i<len(diff) and j<len(buttons):
  if diff[i]>=buttons[j]:
   incompleteTasks+=diff[i]-buttons[j]
   i+=1
   j+=1
  else:
   j+=1
 while i<len(diff):
  incompleteTasks+=diff[i]
  i+=1
 return incompleteTasks


from sys import stdin
t=int(stdin.readline())
while t>0:
 n,k,m=list(map(int,stdin.readline().split()))
 planned=list(map(int,stdin.readline().split()))
 completed=list(map(int,stdin.readline().split()))
 white=list(map(int,stdin.readline().split()))
 black=list(map(int,stdin.readline().split()))
 buttons=white+black
 buttons.sort(reverse=True)
##    print buttons
 diff=[]
 for i in range(n):
  diff.append(planned[i]-completed[i])
 diff.sort(reverse=True)
##    print diff
 print(minTasks(diff,buttons))
 t-=1
