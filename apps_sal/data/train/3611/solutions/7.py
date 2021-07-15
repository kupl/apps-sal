def ranking(people):
    new = sorted(people, key=lambda x: (-x['points'], x['name']))
    for i in new:
        i['position'] = new.index(i) + 1
    for i, v in enumerate(new):
        if i == 0:
            continue
        if v['points'] == new[i - 1]['points']:
            v['position'] = new[i - 1]['position']
    return new
