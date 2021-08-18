
def order_weight(strng):
    lis = strng.split(" ")
    c = []
    for word in lis:
        weight = 0
        for num in word:
            weight += int(num)
        x = {}
        x['number'] = word
        x['weight'] = weight
        c.append(x)
    c.sort(key=lambda x: x['number'])
    c.sort(key=lambda x: x['weight'])
    return ' '.join(x['number'] for x in c)
    print(order_weight(strng))
