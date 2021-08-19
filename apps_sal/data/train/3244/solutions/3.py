def cheapest_quote(papers):

    prices = {40: 3.85, 20: 1.93, 10: 0.97, 5: 0.49, 1: 0.10}
    cost = 0

    for price in prices:
        cost += (papers // price) * prices[price]
        papers %= price

    return round(cost, 2)

    # 7kyu kata number one thousand
