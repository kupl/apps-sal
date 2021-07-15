from string import punctuation as p; camelize = lambda s: ''.join([x.capitalize() for x in reduce(lambda a, kv: a.replace(*kv), [(x, ' ') for x in p], s).split(' ')])
