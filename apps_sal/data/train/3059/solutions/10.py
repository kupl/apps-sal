def rain_amount(mm: int) -> str:
    """
    Get the amount of water your plants will need when you have taken into 
    consideration the amount of rain water that is forecast for the day.
    """
    return {
        mm < 40: f"You need to give your plant {40 - mm}mm of water"
    }.get(True, f"Your plant has had more than enough water for today!")
