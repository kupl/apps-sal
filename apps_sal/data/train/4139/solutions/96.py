def rental_car_cost(d: int) -> int:
    """Gives out the total amount for different count days of rent car"""
    cost = d * 40
    if d >= 7:
        return cost - 50
    elif d >= 3:
        return cost - 20
    else:
        return cost
