def rental_car_cost(days: int) -> int:
    """
     Get the total amount for different days(d) according to the rules:
     - every day you rent the car costs $40
     - 7 or more days, you get $50 off your total
     - 3 or more days, you get $20 off your total
    """
    return days * 40 - {days >= 3: 20, days >= 7: 50}.get(True, 0)
