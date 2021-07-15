# cook your dish here
for _ in range(int(input())):
 l,r = map(int,input().split())
 c = 0
 for i in range(l,r+1):
  if str(i)[-1] in '239':
   c += 1
 print(c)
