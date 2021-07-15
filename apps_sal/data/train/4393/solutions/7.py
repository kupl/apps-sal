repeat_sum=lambda x:sum(list(set([j for i in x for j in i if sum(1for q in x if j in q)>1])))
