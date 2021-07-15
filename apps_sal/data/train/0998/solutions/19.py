n,q = map(int,input().split())
row = [0]*n
col = [0]*n
for i in range(q):
 s = input()
 if s[0] == 'R':
  r,x = map(int,s.split()[1:])
  row[r-1] += x
 else:
  c,x = map(int,s.split()[1:])
  col[c-1] += x
print(max(row)+max(col))
