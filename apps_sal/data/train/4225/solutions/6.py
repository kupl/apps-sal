def cup_and_balls(b, arr):
    my_ball = b
    for turn in arr:
        if my_ball in turn:
            for x in turn:
                if x != my_ball:
                    my_ball = x
                    break
    return my_ball
