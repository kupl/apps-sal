# cook your dish here
x = int(input())
for k in range(x):
 y = int(input())
 a = list(map(int, input().split()))[:y]
 m = 0
 for i in range(y):
  for j in range(i+1, y):
   if a[i]%2==0 and a[j]%2!=0:
    m+= 1
   else:
    continue
 print(m)
