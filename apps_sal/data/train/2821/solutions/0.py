def trim(beard):
    return [[h.replace('J', '|') for h in b] for b in beard[:-1]] + [['...'] * len(beard[0])]
