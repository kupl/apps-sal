S=input()
N=len(S)
if S[-1]=="1":
    print(-1)
    return
if S[0]=="0":
    print(-1)
    return
if S[-2]=="0":
    print(-1)
    return
for i in range(N-1):
    if S[i]!=S[N-2-i]:
        print(-1)
        return
ans=[]
nowzero=0
for i in range(N):
    if S[i]=="0":
        break
    nowzero+=1
if nowzero==N-1:
    for i in range(1,N):
        print(i,i+1)
    return
ans.append((1,2))
for i in range(N-2):
    if S[i]=="1":
        if i!=N-2 and S[i+1]=="0":
            nowzero=i+2
        ans.append((i+2,i+3))
    else:
        ans.append((nowzero,i+3))
for line in ans:
    print(line[0],line[1])
