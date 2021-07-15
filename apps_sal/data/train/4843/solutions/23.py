choose_best_sum=lambda t,k,l:max((d for d in map(sum,__import__('itertools').combinations(l,r=k))if d<=t),default=None)
