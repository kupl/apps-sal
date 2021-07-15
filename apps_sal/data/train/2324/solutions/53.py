from networkx import*
N,*t=map(str.split,open(0))
s=shortest_path_length
x=s(G:=Graph(t),'1')
y=s(G,*N)
print('FSennunkeec'[sum(x[k]>y[k]for k in x)*2>=len(x)::2])
