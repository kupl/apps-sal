t = int(input())
while t:
 n,m = [int(x) for x in input().split()]
 job_done = [int(x) for x in input().split()]
 li = []
 for i in range(1,n+1):
  if i not in job_done:
   li.append(i)
 chef = []
 assis = []
 for i in range(len(li)):
  if i&1: 
   assis.append(li[i])
  else:
   chef.append(li[i])
   
 print(*chef)
 print(*assis)
 t=t-1
