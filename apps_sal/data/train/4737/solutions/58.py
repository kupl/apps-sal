def fuel_price(litres, price_per_liter):
    disc = litres // 2
    tot_disc = 0
    if disc >= 5:
        tot_disc = 0.25
    else:
        tot_disc = disc * .05
    return round(litres * (price_per_liter - tot_disc),2)
