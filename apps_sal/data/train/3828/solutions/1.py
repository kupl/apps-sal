CHARGE_CONFIG = ((0.85, 1), (0.1, 0.5), (0.05, 0.2))


def calculate_time(battery, charger):
    return round(0.0001 + sum((battery * pb / (charger * pc) for (pb, pc) in CHARGE_CONFIG)), 2)
