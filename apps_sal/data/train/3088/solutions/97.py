def nba_extrap(ppg, mpg):
    # try to do the maths
    try:
        # extrapolate the correct int to multiply by
        relative_minutes = (48 / mpg)
        relative_points = round(ppg * relative_minutes, 1)
    except:
        # if the mpg is zero, it will fail, so set the final answer to 0
        relative_points = 0
    return relative_points
