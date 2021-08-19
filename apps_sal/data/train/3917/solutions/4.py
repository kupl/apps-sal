def freeway_game(distance, speed, cars):
    score = 0
    exit = 60 * distance / speed
    for (other_time, other_speed) in cars:
        other_exit = 60 * distance / other_speed + other_time
        if other_time < 0 and other_exit > exit:
            score += 1
        elif other_time > 0 and other_exit < exit:
            score -= 1
    return score
