def over_the_road(address, street_length):
    if address % 2 == 1:
        positionFromBottom = street_length - address // 2
        return 2 * positionFromBottom
    if address % 2 == 0:
        positionFromTop = street_length - address // 2 + 1
        return 2 * (positionFromTop-1) + 1
