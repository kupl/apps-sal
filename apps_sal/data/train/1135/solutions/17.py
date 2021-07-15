# cook your dish here
t = int(input())
for i in range(t):
  n, k = map(int,input().split())
  din=list(range(1,n+1))
  form=din[-(k+1):]
  form+=(din[0:-(k+1)])
  print(*form)
