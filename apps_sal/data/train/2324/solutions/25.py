from networkx import*
N,*t=open(0)
G=Graph()
for s in t:a,b=s.split();G.add_edge(a,b)
s=shortest_path_length
x=s(G,'1')
y=s(G,N[:-1])
print('FSennunkeec'[sum(x[k]>y[k]for k in x)*2>=int(N)::2])
