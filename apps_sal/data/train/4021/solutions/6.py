elections_winners=lambda v,k:v.sort()or sum(e+k>v[-1]for e in v)or v.count(v[-1])==1
