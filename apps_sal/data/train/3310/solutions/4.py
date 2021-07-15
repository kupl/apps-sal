def score_pole_vault(vaulter_list):
    r={}
    for v in vaulter_list:
        x=[len(v['results']),0,0]
        f=0
        for i,t in enumerate(v['results'][::-1]):
            if 'O' in t and x[0]==len(v['results']):
                x=[i,t.count('X'),0]
            f+=t.count('X')
        x[2]=f
        r[v['name']]=tuple(x)
    rank=sorted(list(r.keys()),key=lambda x:r[x])
    first=[rank[0]]
    second=[]
    third=[]
    for name in rank[1:]:
        if r[first[0]]==r[name]:
            first.append(name)
        elif not second or r[second[0]]==r[name]:
            second.append(name)
        elif not third or r[third[0]]==r[name]:
            third.append(name)
    if len(first)>=2:
        d={'1st': ', '.join(sorted(first))+' (jump-off)'}
        if len(first)==2:
            if len(second)==1:
                d['3rd']=second[0]
            else:
                d['3rd']=', '.join(sorted(second))+' (tie)'
    else:
        d={'1st': first[0]}
        if len(second)>=2:
            d['2nd']=', '.join(sorted(second))+' (tie)'
        else:
            d['2nd']=second[0]
            if len(third)==1:
                d['3rd']=third[0]
            else:
                d['3rd']=', '.join(sorted(third))+' (tie)'
    return d

