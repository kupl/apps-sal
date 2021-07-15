def find_the_ball(start, swaps):
    for sw in swaps:
        if start in sw:
            start = sw[1-sw.index(start)]
    return start
