for _ in range (int(input())):
 a = int(input())
 ass = list(map(int , input().split()))
 b = 0
 for i in range(a):
  if ass.count(ass[i]) > b:
   b = ass.count(ass[i])
 print(a - b)

