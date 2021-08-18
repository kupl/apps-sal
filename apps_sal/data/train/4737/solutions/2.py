from bisect import bisect


def fuel_price(litres, price_per_liter):
    discount = (0, 5, 10, 15, 20, 25)[bisect([2, 4, 6, 8, 10], litres)] * 0.01
    return (litres * price_per_liter) - (litres * discount)


fuelPrice = fuel_price
