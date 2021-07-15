def not_so_random(b,w):
    # If we pick 2 black we replace with white (Net black -2)
    # if we pick 1 black and 1 white we replace with black (Net black = 0)
    # if we pick 2 white we replace with one white (Net black = 0)
    return ['White', 'Black'][b % 2]
