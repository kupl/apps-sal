# cook your dish here
n = int(input())
l = []
for i in range(n):
 a, h = map(int,input().split())
 l.append([a,h])
if len(l)==1:
 print(1)
 return
p = l[0][0]
count = 2
for i in range(1,len(l)-1):
 if l[i][0]-l[i][1]>p:
  p = l[i][0]
  count+=1
 elif l[i][0]+l[i][1]<l[i+1][0]:
  p = l[i][0]+l[i][1]
  count+=1
 else:
  p = l[i][0]
print(count)
