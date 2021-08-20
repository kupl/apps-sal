def calculate_time(bat, charger):
    return round(bat * 0.85 / charger + bat * 0.1 / (charger * 0.5) + bat * 0.05 / (charger * 0.2), 2)
