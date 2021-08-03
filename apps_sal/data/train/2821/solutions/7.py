def trim(beard):
    return [[c.replace('J', '|') for c in row] for row in beard[:-1]] + [['...'] * len(beard[-1])]
