def freeway_game(dist_km_to_exit, my_speed_kph, other_cars):
    score = 0
    for pair in other_cars:
        if my_speed_kph == pair[1]:
            continue
        if 0 < pair[1] * (pair[0] / 60) / (pair[1] - my_speed_kph) < dist_km_to_exit / my_speed_kph:
            score = score - 1 if pair[0] > 0 else score + 1
    return score
