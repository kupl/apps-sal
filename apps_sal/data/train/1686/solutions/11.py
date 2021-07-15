#for _ in range(int(input())):
#dt = {} for i in x: dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}
ipnl = lambda n: [int(input()) for _ in range(n)]
inp = lambda :int(input())
ip = lambda :[int(w) for w in input().split()]
mp = lambda :map(int,input().split())

r,c,d = mp()
x = [[{'D':0,'R':0,'CT':0,'f':1} for i in range(c+1)] for j in range(r+1)]
for i in range(1,r+1):
    t = ip()
    for j in range(c):
        if t[j] == 0:
           x[i][j+1]['f'] = 2
for i in range(1,r+1):
    for j in range(1,c+1):
        flag = 0
        if i==1 and j==1:
            x[i][j] = {'D':0,'R':0,'CT':1,'f':0}
        elif x[i][j]['f'] != 2:
            x[i][j] = {'D':0,'R':0,'CT':0,'f':0}
            #from up
            if x[i-1][j]['f'] == 0 and x[i-1][j]['D'] < d:
                flag += 1
                x[i][j]['D'] = x[i-1][j]['D'] + 1
                x[i][j]['CT'] += x[i-1][j]['CT']
            #from left
            if x[i][j-1]['f'] == 0 and x[i][j-1]['R'] < d:
                flag += 1
                x[i][j]['R'] = x[i][j-1]['R'] + 1
                x[i][j]['CT'] += x[i][j-1]['CT']
            if flag == 0:
                x[i][j] = {'D':0,'R':0,'CT':0,'f':2}
print(x[r][c]['CT']%20011)
"""
for i in range(r+1):
    print(*x[i])
"""
