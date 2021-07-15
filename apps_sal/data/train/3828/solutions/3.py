def calculate_time(battery,charger):
    return round(1e-10 + 1.3 * battery / charger, 2)
