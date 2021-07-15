counting_triangles=lambda V:(lambda v,W:sum([W[k]<W[i]+W[j]for i in range(v)for j in range(i+1,v)for k in range(j+1,v)]))(len(V),sorted(V))
