# cook your dish here
'''test=int(input())
for _ in range(test):
    r,c=map(int,input().split())
    
    pathant=[]
    rc=[]
    for i in range(r):
        ci=list(map(str,input()))
        rc.append(ci)
        for j in range(c):
            if(ci[j]!='#' and ci[j]!='-'):
                pathant.append([ci[j],i,j])
            
    count=0
    parr=[]
    print(pathant)
    for i in range(len(pathant)):
        temp=[]
        if(pathant[i][0]=='L'):
            count=pathant[i][2]
            for j in range(count,-1,-1):
                if(rc[pathant[i][1]][j]=='#'):
                    break
                temp.append([pathant[i][1],j])
            parr.append(temp)
        if(pathant[i][0]=='R'):
            count=pathant[i][2]
            for j in range(count,c):
                if(rc[pathant[i][1]][j]=='#'):
                    break
                temp.append([pathant[i][1],j])
            parr.append(temp)
        if(pathant[i][0]=='U'):
            count=pathant[i][1]
            for j in range(count,-1,-1):
                if(rc[j][pathant[i][2]]=='#'):
                    break
                temp.append([j,pathant[i][2]])
            parr.append(temp)
        if(pathant[i][0]=='D'):
            count=pathant[i][1]
            for j in range(count,r):
                if(rc[j][pathant[i][2]]=='#'):
                    break
                temp.append([j,pathant[i][2]])
            parr.append(temp)
    print(parr)
    length=len(parr)
    noe=[0]*len(parr)
    nop=0
    pointer=0
    lim=max(r,c)
    temp=[]
    while pointer < lim:
        temp=[]
        for x in range(length):
            if(pointer<=len(parr[x])):
                temp.append(parr[x][pointer])'''

from collections import defaultdict as df
t = int(input())
for x in range(t):
    r, c = list(map(int, input().split()))
    p = df(list)
    a = [[0] * c for i in range(r)]
    for i in range(r):
        s = input().rstrip()
        for j in range(c):
            a[i][j] = s[j]
    for i in range(r):
        for j in range(c):
            timer = 0
            if a[i][j] == 'U':

                for k in range(i - 1, -1, -1):
                    if a[k][j] != '#':
                        timer += 1
                        p[str(k) + ' ' + str(j)].append(timer)
                    else:
                        break
            if a[i][j] == 'R':
                for k in range(j + 1, c):
                    if a[i][k] != '#':
                        timer += 1
                        p[str(i) + ' ' + str(k)].append(timer)
                    else:
                        break
            if a[i][j] == 'D':
                for k in range(i + 1, r):
                    if a[k][j] != '#':
                        timer += 1
                        p[str(k) + ' ' + str(j)].append(timer)
                    else:
                        break
            if a[i][j] == 'L':
                for k in range(j - 1, -1, -1):
                    if a[i][k] != '#':
                        timer += 1
                        p[str(i) + ' ' + str(k)].append(timer)
                    else:
                        break
    # print(p)
    total = 0
    # print(p)
    for i in p:
        y = set(p[i])
        for j in y:
            if p[i].count(j) > 1:
                n1 = p[i].count(j)
                total += (n1 * (n1 - 1)) // 2
    print(total)
