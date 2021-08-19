def freeway_game(dist_km_to_exit, my_speed_kmph, other_cars):
    my_time_to_exit = dist_km_to_exit / my_speed_kmph
    return sum((+(lead < 0 and my_time_to_exit * speed < dist_km_to_exit + lead / 60 * speed) - (lead > 0 and my_time_to_exit * speed > dist_km_to_exit + lead / 60 * speed) for (lead, speed) in other_cars))
