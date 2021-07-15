import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def ng():
    if s[0]=="0" or s[-1]=="1":return True
    for i in range(n):
        if i>n-2-i:break
        if s[i]!=s[n-2-i]:return True
    return False

s=SI()
n=len(s)

if ng():
    print(-1)
    return

aa=[]
for i in range(n//2):
    if s[i]=="1":aa.append(i+1)
aa.append(n)

ans=[]
for i in range(len(aa)-1):ans.append([i+1,i+2])

j=len(aa)+1
for i,(a0,a1) in enumerate(zip(aa,aa[1:])):
    for _ in range(a1-a0-1):
        ans.append([i+2,j])
        j+=1

for u,v in ans:print(u,v)

