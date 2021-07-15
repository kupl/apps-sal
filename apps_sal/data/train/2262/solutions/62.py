def f(r,c):
    if c==0: return r
    elif c==C: return R+C+(R-r)
    elif r==0: return R*2+C+(C-c)
    elif r==R: return R+c
    else: return -1

import sys
input = sys.stdin.readline
R,C,N=map(int, input().split())
Q=[]
l=1
for i in range(N):
    r0,c0,r1,c1=map(int, input().split())
    if f(r0,c0) != -1 and f(r1,c1) != -1:
        s,t=f(r0,c0),f(r1,c1)
        if s>t: s,t=t,s
        Q.append((s,l))
        Q.append((t,-l))
        l+=1
Q.sort(key=lambda x:x[0])
flg=True
R=[]
for _, q in Q:
    if q>0:
        R.append(q)
    elif q<0:
        if not R: flg=False; break
        p=R.pop()
        if -p!=q: flg=False; break
print("YES" if flg else "NO")
