def repeat_sum(x):
    return sum(list(set([j for i in x for j in i if sum((1 for q in x if j in q)) > 1])))
