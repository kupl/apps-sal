def queue_battle(dist, *armies0):
    armies = [{'idx': idx, 'soldier': [{'idx': idx, 'speed': el, 'remove': False} for (idx, el) in enumerate(a)]} for (idx, a) in enumerate(armies0)]
    bullets = [[] for i in range(len(armies))]
    while len(armies) > 1:
        for i in range(len(bullets)):
            bullets2 = list(filter(lambda d: d['dist'] < dist, map(lambda d: {'dist': d['dist'] + d['speed'], 'speed': d['speed']}, bullets[i])))
            if len(bullets2) != len(bullets[i]):
                armies[(i + 1) % len(armies)]['soldier'][0]['remove'] = True
            bullets[i] = bullets2
        armies = list(filter(lambda a: not (len(a['soldier']) == 1 and a['soldier'][0]['remove']), armies))
        elimination = len(armies) != len(bullets)
        for i in range(len(armies)):
            el = armies[i]['soldier'].pop(0)
            if not el['remove']:
                bullets[i].append({'dist': 0, 'speed': el['speed']})
                armies[i]['soldier'].append(el)
        if elimination:
            bullets = [[] for i in range(len(armies))]
    if len(armies) > 0:
        return (armies[0]['idx'], tuple(map(lambda s: s['idx'], armies[0]['soldier'])))
    return (-1, ())
