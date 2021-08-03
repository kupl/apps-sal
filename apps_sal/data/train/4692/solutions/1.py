def max_profit(prices):
    out = prices[1] - prices[0]
    min_price = prices[0]

    for i in prices[1:]:
        if i - min_price > out:
            out = i - min_price
        if i < min_price:
            min_price = i
    return out
