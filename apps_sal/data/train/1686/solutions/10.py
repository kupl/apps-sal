#for _ in range(int(input())):
#dt = {} for i in x: dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}
ipnl = lambda n: [int(input()) for _ in range(n)]
inp = lambda :int(input())
ip = lambda :[int(w) for w in input().split()]
mp = lambda :map(int,input().split())

r,c,d = mp()
x = [[{'D':0,'R':0,'f':1} for i in range(c)] for j in range(r)]
for i in range(r):
    t = ip()
    for j in range(c):
        if t[j] == 0:
            x[i][j] = {'D':0,'R':0,'f':0}
x[0][0] = {'D':1,'R':1,'f':1}
for i in range(r):
    for j in range(c):
        if x[i][j]['f']:
            ind = i-1
            ctr = 0
            while ind>=0 and ctr < d and x[ind][j]['f']:
                x[i][j]['D'] += x[ind][j]['R']
                ind -= 1
                ctr += 1
            ind = j-1
            ctr = 0
            while ind>=0 and ctr < d and x[i][ind]['f']:
                x[i][j]['R'] += x[i][ind]['D']
                ind -= 1
                ctr += 1
ans = x[-1][-1]['R'] + x[-1][-1]['D']
print(ans%20011)
