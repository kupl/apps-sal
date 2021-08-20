def fuel_price(l, ppl):
    if l >= 10:
        ppl -= 0.25
        return round(l * ppl, 2)
    elif l >= 8:
        ppl -= 0.2
        return round(l * ppl, 2)
    elif l >= 6:
        ppl -= 0.15
        return round(l * ppl, 2)
    elif l >= 4:
        ppl -= 0.1
        return round(l * ppl, 2)
    elif l >= 2:
        ppl -= 0.05
        return round(l * ppl, 2)
    return round(l * ppl, 2)
