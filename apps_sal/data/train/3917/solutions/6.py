def freeway_game(dist_km_to_exit, my_speed_kph, other_cars):

    def f_time(s):
        return dist_km_to_exit / s * 60
    duration = f_time(my_speed_kph)
    c = 0
    for (p, s) in other_cars:
        t = f_time(s) + p
        c += (t > duration and p < 0) - (t < duration and p > 0)
    return c
