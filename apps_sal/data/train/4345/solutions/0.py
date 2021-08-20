def buy_or_sell(pairs, harvested_fruit):
    currentFruit = harvested_fruit
    actions = list()
    for pair in pairs:
        if currentFruit not in pair:
            return 'ERROR'
        if currentFruit == pair[0]:
            actions.append('buy')
            currentFruit = pair[1]
        else:
            actions.append('sell')
            currentFruit = pair[0]
    return actions
