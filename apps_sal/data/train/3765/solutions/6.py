def highest_age(group1,group2):
    total={}
    
    for p in group1+group2:
        total[p['name']] = total.get(p['name'],0)+p['age']
    
    return sorted(total, key=total.__getitem__)[-1]
