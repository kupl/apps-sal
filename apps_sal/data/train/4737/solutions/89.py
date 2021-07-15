def fuel_price(litres, price_per_liter):
    if litres>=2 and litres<4:
        price_per_liter = price_per_liter - 0.05
    elif litres>=4 and litres<6 :
        price_per_liter = price_per_liter - 0.10
    elif litres>=6 and litres<8 :
        price_per_liter = price_per_liter - 0.15
    elif litres>=8 and litres<10 :
        price_per_liter = price_per_liter - 0.20
    elif litres>=10  :
        price_per_liter = price_per_liter - 0.25
    return litres*price_per_liter
