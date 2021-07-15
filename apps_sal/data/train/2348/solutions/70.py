n = int(input())
hot = list(map(int,input().split())) 
n_ = n.bit_length()
db = [[n-1]*(n)]
L = int(input())
r = 1
for i in range(n-1):
  while r < n-1 and hot[r+1]-hot[i] <= L:
    r += 1
  db[0][i] = r
for j in range(1,n_+1):
  new = [db[-1][db[-1][i]] for i in range(n)]
  db.append(new)
  if new[0] == n-1:
    break
n_ = len(db)

def query(s,t):
  dt = 0
  for j in range(n_-1,0,-1):
    if db[j][s] < t:
      dt += 2**j
      s = db[j][s]
  while s < t:
    dt += 1
    s = db[0][s]
  return dt 

q = int(input())
for _ in range(q):
  s,t = list(map(int,input().split()))
  if t < s:
    s,t = t,s
  print((query(s-1,t-1)))

