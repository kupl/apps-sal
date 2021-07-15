def freeway_game(dist_km_to_exit, my_speed, other_cars):
    count = 0
    for (other_start_minute, other_speed) in other_cars:
        if other_speed == my_speed:
            continue
        other_start_time = other_start_minute / 60
        passing_point = (
            (other_start_time * my_speed * other_speed) /
            (other_speed - my_speed)
        )
        if 0 < passing_point < dist_km_to_exit:
            if my_speed > other_speed:
                count += 1
            else:
                count -= 1  
    return count
