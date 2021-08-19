def trim(beard):
    return [['|' if j in ['|', 'J'] else j for j in i] for i in beard[:-1]] + [['...'] * len(beard[-1])]
