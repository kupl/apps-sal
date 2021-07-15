S = input()
T = input()
n = len(S)
m = len(T)
L = [0]*(n+1)
R = [0]*(m+1)
for i, s in enumerate(S):
  if s == "A":
    L[i+1] = (L[i]+1)%3
  else:
    L[i+1] = (L[i]-1)%3
for i, t in enumerate(T):
  if t == "A":
    R[i+1] = (R[i]+1)%3
  else:
    R[i+1] = (R[i]-1)%3
q = int(input())
for _ in range(q):
  a, b, c, d = map(int, input().split())
  if (L[b]-L[a-1])%3 == (R[d]-R[c-1])%3:
    print("YES")
  else:
    print("NO")
