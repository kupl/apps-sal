def zero_fuel(pump, miles, gallons):
    """berechnet ob der Tank zur Tanke reicht"""
    return miles * gallons >= pump
