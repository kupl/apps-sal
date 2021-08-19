def bouncing_ball(initial, proportion):
    height_now = initial
    counter = 0
    while height_now > 1:
        height_now *= proportion
        counter += 1
    return counter
