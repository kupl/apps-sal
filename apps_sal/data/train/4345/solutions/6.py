def buy_or_sell(pairs, harvested_fruit):
    result = []
    fruit = harvested_fruit
    for a, b in pairs:
        if fruit == a:
            result.append('buy')
            fruit = b
        elif fruit == b:
            result.append('sell')
            fruit = a
        else:
            return 'ERROR'
    if fruit != harvested_fruit:
        return 'ERROR'
    return result

