def fuel_price(l, ppl):
    if l < 2:
        return l * ppl
    elif l < 4:
        return l * ppl - 0.05 * l
    elif l < 6:
        return l * ppl - 0.1 * l
    elif l < 8:
        return l * ppl - 0.15 * l
    elif l < 10:
        return l * ppl - 0.2 * l
    return l * ppl - 0.25 * l
