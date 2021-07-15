n,d = list(map(int,input().split()))
l = []
c = 0
for i in range(n):
 s = int(input())
 l.append(s)
l.sort()
i = 0
while(i<n-1):
 if(l[i+1]-l[i]<=d):
  c = c+1
  i = i+2
 else:
  i = i+1
print(c)

