for _ in range(int(input())):
    r,c=map(int,input().split())
    d=[]
    s=0
    for _ in range(r):
        a=input()
        a=[i for i in a]
        d.append(a)
    for i in range(r):
        for j in range(c):
            if d[i][j]=='R':
                for k in range(j,c):
                    if d[i][k]=='#':break
                    elif d[i][k]=='L' and not((k-j) & 1):s+=1
                l=i+1
                k=j+1
                while k<c and l<r:
                    f=0
                    if d[l][k]=='U':
                        for m in range(j,k+1):
                            if d[i][m]=='#':
                                f=1
                                break
                        if f==0:
                         for m in range(i,l+1):
                             if d[m][k]=='#':
                                 f=1
                                 break
                        if f==0:s+=1
                    k+=1
                    l+=1
            elif d[i][j]=='L':
                l=i+1
                k=j-1
                while l<r and k>-1:
                  if d[l][k]=='U':
                    f=0
                    for m in range(j,k-1,-1):
                        if d[i][m] == '#':
                            f = 1
                            break
                    if f == 0:
                        for m in range(i,l+1):
                            if d[m][k] == '#':
                                f=1
                                break
                    if f == 0: s += 1
                  l+=1
                  k-=1
            elif d[i][j]=='D':
                for m in range(i,r):
                    if d[m][j]=='#':break
                    elif d[m][j]=='U' and not((m-i) & 1):s+=1
                l=i+1
                k=j+1
                while l<r and k<c:
                    f=0
                    if d[l][k]=='L':
                        for m in range(i,l+1):
                            if d[m][j] == '#':
                                f = 1
                                break
                        if f == 0:
                            for m in range(j,k+1):
                                if d[l][m] == '#':
                                    f = 1
                                    break
                        if f == 0: s += 1
                    l += 1
                    k += 1
                l=i+1
                k=j-1
                while l<r and k>-1:
                    f=0
                    if d[l][k]=='R':
                        for m in range(i,l+1):
                            if d[m][j]=='#':
                                f=1
                                break
                        if f==0:
                            for m in range(k,j+1):
                                if d[l][m]=='#':
                                    f=1
                                    break
                        if f==0:s+=1
                    l+=1
                    k-=1
    print(s)
