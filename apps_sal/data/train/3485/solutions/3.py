def separate_liquids(glass):
    chain = sorted(sum(glass, []), key = 'HWAO'.index)
    return [[chain.pop() for c in ro] for ro in glass]
