def fuel_price(litres, price_per_liter):
    discount = [0, 0.05, 0.1, 0.15, 0.2, 0.25]
    try:
        sale = discount[litres // 2]
    except IndexError:
        sale = max(discount)
    return litres * price_per_liter - litres * sale
