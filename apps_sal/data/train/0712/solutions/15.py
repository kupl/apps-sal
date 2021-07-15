for _ in range(int(input())):
 n = int(input())
 l = list(map(int, input().split()))
 
 flag = 0
 for i in l:
  if i % 2 == 0:
   flag = 1
   break
 
 if flag:
  print("NO")
 else:
  print("YES")
