def buy_or_sell(pairs, fruit):
    result = []
    for pair in pairs:
        if pair[0] == fruit:
            result.append('buy')
            fruit = pair[1]
        elif pair[1] == fruit:
            result.append('sell')
            fruit = pair[0]
        else:
            return 'ERROR'
    return result
