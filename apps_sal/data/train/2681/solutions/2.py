def bouncing_ball(i, p , n = 0):
    return n if i <= 1 else bouncing_ball(i*p, p, n+1)
