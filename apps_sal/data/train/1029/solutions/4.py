# cook your dish here
t = int(input())
for i in range(t):
 n,m = map(int,input().split())
 done_task = list(map(int,input().split()))
 done_task.sort()
 left_tasks=[]
 chef=[]
 assist=[]
 for i in range(n):
  if i+1 not in done_task:
   left_tasks.append(i+1)
 for i in range(n-m):
  if i%2==0:
   chef.append(left_tasks[i])
  else:
   assist.append(left_tasks[i])
 print(*chef)
 print(*assist)
