def ski_jump(mountain):
    speed = float(len(mountain[-1])) * 1.5
    jump = (len(mountain[-1]) * speed * 9) / 10
    if jump < 10:
        res = "He's crap!"
    elif jump < 25:
        res = "He's ok!"
    elif jump < 50:
        res = "He's flying!"
    else:
        res = "Gold!!"
    return '{:.2f}'.format(jump) + " metres: " + res
