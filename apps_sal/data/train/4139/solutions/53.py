def rental_car_cost(days):
    return days * 40 - 20 * (days >= 3 and days < 7) - 50 * (days >= 7)
