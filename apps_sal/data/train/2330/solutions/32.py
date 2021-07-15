import sys
S = input()
N = len(S)
ss = S[:N-1]
if S[-1] == '1' or ss != ss[::-1] or S[0] == '0':
    print((-1))
    return
tree = []
cnt = 0
for s in ss:
    if s == '1':
        tree.append(cnt)
        cnt = 0
    else:
        cnt += 1
ans = []
now = 1
for c in tree:
    for i in range(c):
        ans.append((now, now+i+1))
    ans.append((now, now+c+1))
    now = now+c+1
for a, b in ans:
    print((a, b))
        
    






    



