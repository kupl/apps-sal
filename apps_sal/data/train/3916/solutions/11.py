mean_vs_median=lambda n:'mean'if sum(n)/len(n)>n[int(len(n)/2)]else'same'if sum(n)/len(n)==n[int(len(n)/2)+1]else"median"
