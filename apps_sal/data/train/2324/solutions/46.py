from networkx import*
(N,), *t = [s.split()for s in open(0)]
G = Graph()
for a, b in t:
    G.add_edge(a, b)
s = shortest_path_length
x = s(G, '1')
y = s(G, N)
c = 0
for k in y:
    c += x[k] > y[k]
print('FSennunkeec'[c * 2 >= int(N)::2])
