def ranking(people):
    x = sorted(sorted(people, key=lambda i: i['name']), key=lambda i: i['points'], reverse=True)
    for i in range(len(x)):
        x[i]['position'] = i + 1
        if i > 0:
            if x[i - 1]['points'] == x[i]['points']:
                x[i]['position'] = x[i - 1]['position']
    return x
