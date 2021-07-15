from itertools import combinations as comb
strings_crossover=lambda li,r:sum(all(r[k] in [i[0][k],i[1][k]] for k in range(len(i[0]))) for i in comb(li,2))
