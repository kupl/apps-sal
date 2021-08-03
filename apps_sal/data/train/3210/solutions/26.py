def get_strings(city):
    res = {}
    for i in city.lower().replace(' ', ''):
        res[i] = res.get(i, '') + '*'

    return ','.join([f'{k}:{v}' for k, v in res.items()])
