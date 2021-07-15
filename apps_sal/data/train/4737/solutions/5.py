def fuel_price(litres: int, price_per_liter: int) -> float:
    return litres * (price_per_liter - 0.05 * min(litres // 2, 5))

