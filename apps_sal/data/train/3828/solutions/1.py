CHARGE_CONFIG = ((.85, 1), (.1, .5), (.05, .2)) 

def calculate_time(battery, charger):
    return round(1e-4 + sum(battery * pb / (charger * pc) for pb,pc in CHARGE_CONFIG), 2)
