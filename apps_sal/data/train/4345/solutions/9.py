def buy_or_sell(pairs, harvested_fruit):
    result = []
    for i in pairs:
        if i[0] == harvested_fruit:
            result.append("buy")
            harvested_fruit = i[1]
        elif i[1] == harvested_fruit:
            result.append("sell")
            harvested_fruit = i[0]
        else:
            return "ERROR"
    return result
