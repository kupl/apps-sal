def fuel_price(l, ppl):
    return round(l * (ppl - min(l // 2 * .05, .25)), 2)
