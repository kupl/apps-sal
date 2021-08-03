def over_the_road(address, n):
    house_index = (n * 2 - address) / 2 if address % 2 == 0 else (address - 1) / 2
    return house_index * 2 + 1 if address % 2 == 0 else (n * 2) - (house_index * 2)
