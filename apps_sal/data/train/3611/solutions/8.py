ranking=lambda p:p.sort(key=lambda e:(-e['points'],e['name']))or[e.update({'position':[x['points']for x in p].index(e['points'])+1})or e for e in p]
