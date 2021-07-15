def cup_and_balls(b, arr):
    for switch in arr:
        if b in switch:
            b = sum(switch) - b
    return b
