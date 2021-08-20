def diamonds_and_toads(sentence, fairy):
    items = {'ruby': 0, 'crystal': 0} if fairy == 'good' else {'python': 0, 'squirrel': 0}
    for key in items.keys():
        items[key] = sentence.count(key[0]) + 2 * sentence.count(key[0].upper())
    return items
