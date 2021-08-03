def bouncing_ball(initial, proportion):
    height_now = initial         # ball height now.
    counter = 0                  # counter for number of jumb initially zero
    while height_now > 1:        # stay in while loop until height is smaller than than1
        height_now *= proportion
        counter += 1             # each time we iterate in while increase count of jump by 1
    return counter             # return number of jump
