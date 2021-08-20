def billboard(name, price=30):
    """No multiplier operator."""
    myPrice = [price for char in name]
    return sum(myPrice)
