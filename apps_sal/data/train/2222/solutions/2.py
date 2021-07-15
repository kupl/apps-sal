def dfs(x,y):
    nonlocal f
    pos.append((x,y))
    y+=1
    if f or str(gr[x][y]).isalpha():
        return
    if y>=q-1:
        f=True
        return
    if not str(gr[x][y+1]).isalpha():
        if not str(gr[x][y+2]).isalpha():
            if (x,y+2) not in pos:
                dfs(x,y+2)
    if x>0:
        if not str(gr[x-1][y]).isalpha():
            if not str(gr[x-1][y+1]).isalpha():
                if not str(gr[x-1][y+2]).isalpha():
                    if (x-1,y+2) not in pos:
                        dfs(x-1,y+2)
    if x<2:
        if not str(gr[x+1][y]).isalpha():
            if not str(gr[x+1][y+1]).isalpha():
                if not str(gr[x+1][y+2]).isalpha():
                    if (x+1,y+2) not in pos:
                        dfs(x+1,y+2)


n=int(input())
for i in range(n):
    q,w=[int(i) for i in input().split()]
    gr=list()
    gr.append(input()+"     ")
    gr.append(input()+"     ")
    gr.append(input()+"     ")
    pos=[]
    f=False
    for i in range(3):
        if gr[i][0]=='s':
            gr[i]=" "+gr[i][1:]
            dfs(i,0)
            break
    if f:
        print("YES")
    else:
        print("NO")
