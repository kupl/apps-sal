def bouncing_ball(initial, proportion):
    count = 0
    while initial > 1:
        initial = initial * proportion
        count = count + 1
    return count
