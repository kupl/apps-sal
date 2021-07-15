crossing_sum=lambda m,r,c: sum(m[r])+sum(l[c] for i,l in enumerate(m) if i!=r)
