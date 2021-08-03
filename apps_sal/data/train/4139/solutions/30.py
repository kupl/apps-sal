def rental_car_cost(d):
    return (d * 40 - 50) * (d >= 7) or (d * 40 - 20) * (d >= 3) or d * 40
