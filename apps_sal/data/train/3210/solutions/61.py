def get_strings(city):
    record = []
    text = ''.join(city.split()).lower()
    collect = {}
    counter = 0
    for i in range(len(text)):
        if text[i] not in collect:
            counter = text.count(text[i])
            collect[text[i]] = ':' + counter * '*'
        else:
            counter += 1
    for (x, y) in list(collect.items()):
        record.append(x + y)
    return ','.join(record)
