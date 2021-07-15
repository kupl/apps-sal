def bouncing_ball(initial, p):
    if initial <= 1:
        return 0
    else:
        return 1 + bouncing_ball(initial * p, p)
