m=lambda n,l,a,b,c:n and m(n-1,l,a,c,b)+[l[c].append(l[a].pop())or str(l)]+m(n-1,l,b,a,c)or[]
hanoiArray=lambda n:(lambda l:str(l)+'\n'+'\n'.join(map(str,m(n,l,0,1,2))))([list(range(n,0,-1)),[],[]])
