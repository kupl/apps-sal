try:
 for i in range(int(input())):
  l=list(map(int,input().split()))
  l.sort()
  m=1
  a=l[0]
  b=l[1]
  c=l[2]
  ans=a*(b-1)*(c-2)
  print(ans% ((10**9)+7))
except:
 pass
