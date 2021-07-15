ans=[]
for i in range(int(input())):
 n, r, x, y = list(map(int, input().split()))
 if x>0:
  x=list(map(int, input().split()))
 else:
  x=[]
 if y>0:
  x+=list(map(int, input().split()))
 x=list(set(x))
 ans.append(min(n-len(x), r))
for i in ans:
 print(i)

