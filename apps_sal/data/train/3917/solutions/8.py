def freeway_game(dist_km_to_exit, my_speed_kph, other_cars):
    t0 = dist_km_to_exit / my_speed_kph
    def time_car(dist0, time_delta, speed): return (dist0 + time_delta * speed / 60) / speed
    result = 0
    for car in other_cars:
        if car[0] > 0 and time_car(dist_km_to_exit, car[0], car[1]) < t0:
            result -= 1
            continue
        if car[0] < 0 and time_car(dist_km_to_exit, car[0], car[1]) > t0:
            result += 1
    return result
