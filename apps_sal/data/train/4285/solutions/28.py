def find_slope(p):
    if (p[2] - p[0]) == 0:
        return "undefined"
    else:
        return f'{int((p[3] - p[1]) / (p[2] - p[0]))}'
