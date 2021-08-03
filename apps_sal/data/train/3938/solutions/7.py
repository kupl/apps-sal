def sorted_brands(history):
    d = {}
    for i in history:
        if i['brand'] in d:
            d[i['brand']] += 1
        else:
            d[i['brand']] = 1
    return sorted(list(d.keys()), key=lambda x: d[x], reverse=True)
