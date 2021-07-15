def divide(weight: int) -> bool:
    """Helps to divide a watermelon into two parts even if they have different weight."""
    if weight / 2 >= 2:
        return weight % 2 == 0
    return False
