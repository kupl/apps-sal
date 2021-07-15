#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

s = ins()
t = ins()
sacc = [0]
for c in s:
    sacc.append(((1 if c=='A' else 2)+sacc[-1])%3)
tacc = [0]
for c in t:
    tacc.append(((1 if c=='A' else 2)+tacc[-1])%3)
#ddprint(sacc)
#ddprint(tacc)
q = inn()
for i in range(q):
    a,b,c,d = inm()
    #ddprint('{} {} {} {}'.format(sacc[b],sacc[a-1],tacc[d],tacc[c-1]))
    print('YES' if (sacc[b]-sacc[a-1])%3==(tacc[d]-tacc[c-1])%3 else 'NO')

