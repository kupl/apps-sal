import operator
n, q = map(int, input().split())
x = [0]*(n+1)
y = [0]*(n+1)
for _ in range(q):  
 a = input().split()
 if a[0] == "RowAdd":
  x[int(a[1])] += int(a[2])
 else:
  y[int(a[1])] += int(a[2])
print(max(x) + max(y))
