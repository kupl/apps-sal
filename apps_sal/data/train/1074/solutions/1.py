test = int(input())

for t in range(test):
  n = int(input())
  mark = [0 for i in range(10001)]
  
  logs = list(map(int, input().strip().split()))
  use = []
  
  for log in logs:
    mark[log] += 1
    
    if mark[log]>=2:
      use.append(log)
      
  use = list(set(use))
  #print(use)
  
  #make windows
  full = 0
  half = 0
  
  for log in use:
    full += (mark[log]//4)
    mark[log] = mark[log]%4
    half += (mark[log]//2)
    
  print(full+(half//2))
