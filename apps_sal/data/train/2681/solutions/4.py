def bouncing_ball(x, y, p=1):
    return p if x * y <= 1 else bouncing_ball(x * y, y, p + 1)
