def growing_plant(upSpeed, downSpeed, desiredHeight):
    """growing plant"""
    actual_height = 0
    counter = 0
    while actual_height <= desiredHeight:
        counter += 1
        actual_height += upSpeed
        if actual_height >= desiredHeight:
            return counter
        actual_height -= downSpeed
