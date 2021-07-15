def discover_original_price(price, perc):
    return float('{:0.2f}'.format(price/(1-perc/100)))
