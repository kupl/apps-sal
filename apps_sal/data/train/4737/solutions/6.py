def fuel_price(l, ppl):
    return round(l*(ppl - min(l//2 * 0.05, 0.25)), 2)
