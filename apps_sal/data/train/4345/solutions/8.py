def buy_or_sell(pairs, harvested_fruit):
    fruit = harvested_fruit
    acts = []
    try:
        for pair in pairs:
            act = pair.index(fruit)
            acts.append(['buy', 'sell'][act])
            fruit = pair[1 - act]
        return acts
    except:
        return 'ERROR'
