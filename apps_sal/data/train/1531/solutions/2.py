Nb=int(input())
tree=list(map(int,input().split()))
Ns=int(input())
for i in range(Ns):
    branch,bird=map(int,input().split())
    branch-=1
    bird-=1
    u=bird
    l=tree[branch]-bird-1
    tree[branch]=0
    if branch-1>=0:
        tree[branch-1]+=u
    try:
        tree[branch+1]+=l
    except:pass
    #print(tree)
for nb in tree: 
    print(nb)
