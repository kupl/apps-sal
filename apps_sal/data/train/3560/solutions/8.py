def ski_jump(mountain):
    height = len(mountain)
    speed = height * 1.5
    jumpLength = (height * speed * 9) / 10
    output = {
        10:     " metres: He's crap!",
        25:     " metres: He's ok!",
        50:     " metres: He's flying!",
        1000:    " metres: Gold!!"
    }
    for case in output.keys():
        if (jumpLength < case):
            return "{:.2f}{:s}".format(jumpLength, output.get(case));
