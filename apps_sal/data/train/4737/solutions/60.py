def fuel_price(litres, price_per_liter):
    num_of_discounts = 0
    while num_of_discounts < litres and num_of_discounts < 10:
        price_per_liter -= 0.05
        num_of_discounts += 2
    return round(price_per_liter * litres, 2)
