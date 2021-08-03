from itertools import combinations as comb
def strings_crossover(li, r): return sum(all(r[k] in [i[0][k], i[1][k]] for k in range(len(i[0]))) for i in comb(li, 2))
