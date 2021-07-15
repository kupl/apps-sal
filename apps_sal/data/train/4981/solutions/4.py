def predict(cnd, p):
    wt, res, polls = [], [], {}
    
    for i in p:
        wt.append(i[1])
        res.append(i[0])
    
    wt_sum, res = sum(wt), list(zip(*res))
    
    for i,j in enumerate(cnd):
        polls[j] = round1(sum(k*l for k,l in zip(res[i],wt)) / wt_sum)
    
    return polls
