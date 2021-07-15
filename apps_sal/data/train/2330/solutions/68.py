S=[int(c) for c in input()]
N=len(S)
r=all([S[i]==S[N-i-2] for i in range(N//2)]) and S[0] and not S[-1]
t=[(1,2)]
e=2
for i in range(1,(N-1)//2):
    t.append((e,i+2))
    if S[i]:
        e=i+2
f=1
if N%2==0:
    t.append((e,N-e+1))
    if S[N//2-1]:
        f=0
for i in range(0,(N-1)//2):
    t.append([e if t[i][j]==e and f else (N-e+1 if t[i][j]==N-t[i][j]+1 and f else N-t[i][j]+1) for j in range(2)])
if r:
    print(*[str(l[0])+" "+str(l[1]) for l in t],sep='\n')
else:
    print(-1)
