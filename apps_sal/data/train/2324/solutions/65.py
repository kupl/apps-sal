from networkx import *
((N,), *t) = map(str.split, open(0))
(x, y) = [shortest_path_length(Graph(t), v) for v in ('1', N)]
print('FSennunkeec'[sum((x[k] > y[k] for k in x)) * 2 >= int(N)::2])
