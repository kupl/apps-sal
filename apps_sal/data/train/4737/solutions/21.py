def fuel_price(litres, ppl):
    if litres < 2:
        return round(litres * ppl, 2)
    elif 2 <= litres < 4:
        return round(litres * ppl - litres * 0.05, 2)
    elif 4 <= litres < 6:
        return round(litres * ppl - litres * 0.1, 2)
    elif 6 <= litres < 8:
        return round(litres * ppl - litres * 0.15, 2)
    elif 8 <= litres < 10:
        return round(litres * ppl - litres * 0.2, 2)
    else:
        return round(litres * ppl - litres * 0.25, 2)
