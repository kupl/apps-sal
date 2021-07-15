def over_the_road(address, n):
    
    # Even Number Address
    if address % 2 == 0:
        x = n - address / 2
        return int(1 + 2 * x)
    
    # Odd Number Address
    else:
        x = n - (address + 1) / 2
        return int(2 + 2 * x)

