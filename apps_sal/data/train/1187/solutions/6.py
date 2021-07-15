def help():
 n,m = map(int,input().split(" "))
 max_power = 0

 n1 = n
 while n1>=m:
  n1 = n1//m
  max_power += 1
 sizes = [0]*(max_power+1)

 sizes[max_power] = n//(m**max_power)
 yet = sizes[max_power]
 
 curr = max_power-1
 while curr>=0:
  y1 = n//(m**curr)
  sizes[curr] = y1 - yet
  yet = y1
  curr -= 1

 size = [0]*(max_power+1)
 for i in range(max_power,-1,-1):
  curr = sizes[i]
  size[i] = curr
  for j in range(max_power+1):
   sizes[j] -= curr
 size_ans = 0
 ways_ans = 1
 for i in range(max_power+1):
  C = i+1
  size_ans += size[i]*((C+1)//2)

  if(C%2 == 0):
   ways_ans *= pow((C//2) + 1,size[i],998244353)
   ways_ans = ways_ans % 998244353
 print(size_ans,ways_ans)


for _ in range(int(input())):
 help()
