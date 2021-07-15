def bouncing_ball(h, bounce):
    count = 0
    while h > 1:
        count += 1
        h *= bounce
    return count
