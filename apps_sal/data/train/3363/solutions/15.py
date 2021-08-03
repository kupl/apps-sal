def evaporator(initial_volume, evap_per_day, threshold):
    threshold = float(threshold)

    def loop(current_volume):
        if (is_below_threshold(current_volume)):
            return 0
        else:
            return 1 + loop(decrement_volume(current_volume))

    def decrement_volume(current_volume):
        return current_volume * (1 - evap_per_day / 100.00)

    def is_below_threshold(current_volume):
        return (current_volume / initial_volume) < (threshold / 100.0)

    return loop(float(initial_volume))
