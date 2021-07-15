from sys import stdin, stdout

def readIn():
    return tuple( map(int,input().split()) )

s = input()
sz = len(s)+1
cnt = [ [0]*3 for _ in range(sz) ]
for i in range(sz-1):
    for j in range(3):
        cnt[i+1][j] = cnt[i][j]
    if s[i] == 'x':
        cnt[i+1][0] += 1
    elif s[i] == 'y':
        cnt[i+1][1] += 1
    else :
        cnt[i+1][2] += 1

n = int(input())
res = []
for _ in range(n):
    l,r = readIn()
    tmp = [ cnt[r][i]-cnt[l-1][i] for i in range(3) ]
    res.append( 'YES' if r-l<2 or max(tmp)-min(tmp)<2 else 'NO' )
print('\n'.join(res))
